#!/usr/bin/env python
# coding: utf-8

# In[34]:
#import sys

from app import app
import pandas as pd
import os 
import math
import matplotlib.pyplot as plt
import openpyxl
from time import sleep
import string
from matplotlib.ticker import MaxNLocator
import plotly.express as px
from load_data import get_dataframe , map_id, map_stname, user, opening_range, StartDate, EndDate
from dash import Dash, dcc, html, Input, Output, dash_table
from dash.exceptions import PreventUpdate


df6 = get_dataframe()

# Opening Speed Alarm --> df56
df56 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df56['Current_Station_Opening'] = df56['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df56 = df56.dropna(axis = 0,how ='any')
df56['Current_Station_Opening'] = df56['Current_Station_Opening'].astype("int")
df56['Opening DCU'] = df56['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Door Opening)')
df56['Opening Speed'] = df56['预警描述'].str.extract('(?:.*Door Opening Time)([0.0-9.0]+)')
df56['Opening Speed'] = df56['Opening Speed'].astype("float")
df56 = df56.drop(columns = '预警描述',axis = 1)
df56 = df56.reindex(columns=['车组','车厢','预警时间','Current_Station_Opening','Opening DCU','Opening Speed'])

df56 = df56.dropna(axis = 0 ,how = 'any')
df56 = df56.reset_index(drop=True)


# Opening Time Count in Range  (Group --> 3.0-3.9 , 4.0-4.9 ......  )

df168 = df56.copy()
df168 = df168.drop(df168[df168['Opening Speed'] < 3.7].index, axis = 'rows')
df168['Speed_Range'] = df168['Opening Speed'].apply(lambda op_range : opening_range(op_range))
df168 = pd.DataFrame(df168.groupby(['Speed_Range']).size(),columns=['Opening_Range_Count']).reset_index()
df168['sortout'] = df168['Speed_Range'].str.extract('(?:.*-)([0.0-9.0]+)(?:.9)')
df168['sortout'] = df168['sortout'].astype('int')
df168 = df168.sort_values(by='sortout',ascending = True)
df168.plot.barh(x='Speed_Range',y = 'Opening_Range_Count', rot=0, width = 0.7,figsize = (12,12))
plt.title('Opening_Time_Distribution (Range)')
plt.ylabel('Opening Speed Range')
plt.xlabel('Count')
#plt.savefig(fr'C:/Users/{user}/Downloads/location/Opening_Closing_Time/Distributions/Opening_Time/Opening_Time_Distribution (Range).png')
plt.close()


# In[35]:


# Opening Time Criteria  -->  df61
df61 = df6.copy()
df61['Hi'] = df61['预警描述'].str.extract('(?:.*>)([0.0-9.0]+)(?:)')
df61 = df61.drop(df61[df61['Hi'] == '0'].index, axis = 'rows')
df61 = df61.dropna(axis=0,how='any')
df61.loc[(df61['预警描述'].str.contains('Door Opening Time') == True),'Opening Standard'] = '> ' + df61['Hi']
df61 = df61.dropna(axis = 0, how = 'any')
df61 = pd.DataFrame(df61['Opening Standard'])[:1]
df61 = df61.reset_index(drop = True)


# In[36]:


# Opening Time Excel Files in Dashboard
df58 = df56.copy()
df58 = pd.DataFrame(df58.groupby(['Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
df60 = pd.DataFrame(pd.concat([df56,df61],axis=1))
df60 = df60.set_axis(['车组 (Opening)', '车厢 (Opening)','预警时间 (Opening)', 'Current_Station_Opening','Opening DCU','Opening Speed','Opening Standard'], axis= 'columns')
df60['车厢 (Opening)'] = df60['车厢 (Opening)'].astype(str).str.zfill(2)
df60 = df60.drop(df60[df60['Opening Speed'] < 3.7].index, axis = 'rows')
df60['Source'] = df60['车组 (Opening)']+ '_' + df60['车厢 (Opening)'] + '_' + df60['Opening DCU']
#df60['Type'] = df60['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
#df60['Type'] = 'T' + df60['Type']
df60['Platform ID'] = df60['Current_Station_Opening'].apply(lambda idxx : map_id(idxx))
df60["Current_Station_Opening"]= df60["Current_Station_Opening"].apply(lambda name : map_stname(name))
df60['Speed_Range'] = df60['Opening Speed'].apply(lambda op_range : opening_range(op_range))
df60['sort1']= df60['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df60['sort2']= df60['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
df60['sort3']= df60['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
df60['sort1'] = df60['sort1'].astype("int")
df60['sort2'] = df60['sort2'].astype("int")
df60['sort3'] = df60['sort3'].astype("int")
df60 = df60.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = True)
df60 = df60.fillna('               // ')
df60 = df60.dropna(axis = 0 ,how = 'any')
df60 = df60.reindex(columns=['Source','预警时间 (Opening)','Current_Station_Opening','Platform ID','Opening Speed','Speed_Range','Opening Standard'])


# In[37]:


# Drop Opening Speed if less than 3.7 
df400 = df58.drop(df58[df58['Opening Speed'] < 3.7].index, axis = 'rows')
df400['Opening Speed'] = df400['Opening Speed'].astype('str')


# In[38]:


# Selector of Opening Time (For DropDownList [Trainset])  -->  df114
# Top Ten Opening Time Alarm Graph in Dashboard  -->  df115 
df139 = df56.copy()
df139 = df139.drop(df139[df139['Opening Speed'] < 3.7].index, axis = 'rows')
# Top Ten DCU Opening Time Excel File (Original)  --> df114 
try:
    df114 = df139.copy()
    df114['车厢'] = df114['车厢'].astype(str).str.zfill(2)
    df114['Source'] = df114['车组']+ '_' + df114['车厢'] + '_' + df114['Opening DCU']
    df114['预警时间'] = df114['预警时间'].str.slice(0,10)
    df114 = pd.DataFrame(df114.groupby(['Source','Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
    df114 = df114.reindex(columns=['Source','Opening Speed','Opening Time Count'])
    df115 = df114.nlargest(n = 10 , columns =['Opening Time Count'])
    df115 = df115.sort_values(by='Opening Time Count',ignore_index = True, ascending = False)

except:
    print('No Top Ten DCU Opening Time Result')
# In[39]:


# For sorting the dropdownlist (3.8 --> 25.4)
df403 = pd.DataFrame(df60['Opening Speed'])
df403 = df403.sort_values(by=['Opening Speed'])


# In[40]:


# Top 1 No. of Opening Time Trend (Original) --> df118
try:
 top1 = df115.iloc[0]['Source']
 t1_speed= df115.iloc[0]['Opening Speed']
 df118 = df56.copy()
 df118['车厢'] = df118['车厢'].astype(str).str.zfill(2)
 df118['Source'] = df118['车组']+ '_' + df118['车厢'] + '_' + df118['Opening DCU']
 df118 = df118.loc[(df118['Source'] == top1) & (df118['Opening Speed'] == t1_speed)]
 df118['预警时间'] = df118['预警时间'].str.slice(0,10)
 df118= pd.DataFrame(df118.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df118 = df118.sort_values(by=['预警时间'])
 ax = df118.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df118.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df118['Opening Time Count']))), math.ceil(max(list(df118['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top1 +' '+ 'Opening Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top1 Opening Time Trend')
    plt.close()
    


# In[41]:


#Top 2 No. of Opening Time Trend (Original) --> df119
try:
 top2 = df115.iloc[1]['Source']
 t2_speed= df115.iloc[1]['Opening Speed']
 df119 = df56.copy()
 df119['车厢'] = df119['车厢'].astype(str).str.zfill(2)
 df119['Source'] = df119['车组']+ '_' + df119['车厢'] + '_' + df119['Opening DCU']
 df119 = df119.loc[(df119['Source'] == top2) & (df119['Opening Speed'] == t2_speed)]
 df119['预警时间'] = df119['预警时间'].str.slice(0,10)
 df119= pd.DataFrame(df119.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df119 = df119.sort_values(by=['预警时间'])
 ax = df119.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df119.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df119['Opening Time Count']))), math.ceil(max(list(df119['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top2 +' '+ 'Opening Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top2 Opening Time Trend')
    plt.close()


# In[42]:

#Top 3 No. of Opening Time Trend (Original) --> df120
try:
 top3 = df115.iloc[2]['Source']
 t3_speed= df115.iloc[2]['Opening Speed']
 df120 = df56.copy()
 df120['车厢'] = df120['车厢'].astype(str).str.zfill(2)
 df120['Source'] = df120['车组']+ '_' + df120['车厢'] + '_' + df120['Opening DCU']
 df120 = df120.loc[(df120['Source'] == top3) & (df120['Opening Speed'] == t3_speed)]
 df120['预警时间'] = df120['预警时间'].str.slice(0,10)
 df120= pd.DataFrame(df120.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df120 = df120.sort_values(by=['预警时间'])
 ax = df120.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df120.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df120['Opening Time Count']))), math.ceil(max(list(df120['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top3 +' '+ 'Opening Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top3 Opening Time Trend')
    plt.close()


#Top 4 No. of Opening Time Trend (Original) --> df121
try:
 top4 = df115.iloc[3]['Source']
 t4_speed= df115.iloc[3]['Opening Speed']
 df121 = df56.copy()
 df121['车厢'] = df121['车厢'].astype(str).str.zfill(2)
 df121['Source'] = df121['车组']+ '_' + df121['车厢'] + '_' + df121['Opening DCU']
 df121 = df121.loc[(df121['Source'] == top4) & (df121['Opening Speed'] == t4_speed)]
 df121['预警时间'] = df121['预警时间'].str.slice(0,10)
 df121= pd.DataFrame(df121.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df121 = df121.sort_values(by=['预警时间'])
 ax = df121.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df121.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df121['Opening Time Count']))), math.ceil(max(list(df121['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top4 +' '+ 'Opening Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top4 Opening Time Trend')
    plt.close()


#Top 5 No. of Opening Time Trend (Original) --> df122
try:
 top5 = df115.iloc[4]['Source']
 t5_speed= df115.iloc[4]['Opening Speed']
 df122 = df56.copy()
 df122['车厢'] = df122['车厢'].astype(str).str.zfill(2)
 df122['Source'] = df122['车组']+ '_' + df122['车厢'] + '_' + df122['Opening DCU']
 df122 = df122.loc[(df122['Source'] == top5) & (df122['Opening Speed'] == t5_speed)]
 df122['预警时间'] = df122['预警时间'].str.slice(0,10)
 df122= pd.DataFrame(df122.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df122 = df122.sort_values(by=['预警时间'])
 ax = df122.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df122.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df122['Opening Time Count']))), math.ceil(max(list(df122['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top5 +' '+ 'Opening Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top5 Opening Time Trend)')
    plt.close()


#Top 6 No. of Opening Time Trend (Original) --> df123
try:
 top6 = df115.iloc[5]['Source']
 t6_speed= df115.iloc[5]['Opening Speed']
 df123 = df56.copy()
 df123['车厢'] = df123['车厢'].astype(str).str.zfill(2)
 df123['Source'] = df123['车组']+ '_' + df123['车厢'] + '_' + df123['Opening DCU']
 df123 = df123.loc[(df123['Source'] == top6) & (df123['Opening Speed'] == t6_speed)]
 df123['预警时间'] = df123['预警时间'].str.slice(0,10)
 df123= pd.DataFrame(df123.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df123 = df123.sort_values(by=['预警时间'])
 ax = df123.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df123.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df123['Opening Time Count']))), math.ceil(max(list(df123['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top6 +' '+ 'Opening Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top6 Opening Time Trend')
    plt.close()


#Top 7 No. of Opening Time Trend (Original) --> df124
try:
 top7 = df115.iloc[6]['Source']
 t7_speed= df115.iloc[6]['Opening Speed']
 df124 = df56.copy()
 df124['车厢'] = df124['车厢'].astype(str).str.zfill(2)
 df124['Source'] = df124['车组']+ '_' + df124['车厢'] + '_' + df124['Opening DCU']
 df124 = df124.loc[(df124['Source'] == top7) & (df124['Opening Speed'] == t7_speed)]
 df124['预警时间'] = df124['预警时间'].str.slice(0,10)
 df124= pd.DataFrame(df124.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df124 = df124.sort_values(by=['预警时间'])
 ax = df124.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df124.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df124['Opening Time Count']))), math.ceil(max(list(df124['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top7 +' '+ 'Opening Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()

except:
    print('No Top7 Opening Time Trend')
    plt.close()


#Top 8 No. of Opening Time Trend (Original) --> df125
try:
 top8 = df115.iloc[7]['Source']
 t8_speed= df115.iloc[7]['Opening Speed']
 df125 = df56.copy()
 df125['车厢'] = df125['车厢'].astype(str).str.zfill(2)
 df125['Source'] = df125['车组']+ '_' + df125['车厢'] + '_' + df125['Opening DCU']
 df125 = df125.loc[(df125['Source'] == top8) & (df125['Opening Speed'] == t8_speed)]
 df125['预警时间'] = df125['预警时间'].str.slice(0,10)
 df125= pd.DataFrame(df125.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df125 = df125.sort_values(by=['预警时间'])
 ax = df125.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df125.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df125['Opening Time Count']))), math.ceil(max(list(df125['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top8 +' '+ 'Opening Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()

except:
    print('No Top8 Opening Time Trend')
    plt.close()


#Top 9 No. of Opening Time Trend (Original) --> df126
try:
 top9 = df115.iloc[8]['Source']
 t9_speed= df115.iloc[8]['Opening Speed']
 df126 = df56.copy()
 df126['车厢'] = df126['车厢'].astype(str).str.zfill(2)
 df126['Source'] = df126['车组']+ '_' + df126['车厢'] + '_' + df126['Opening DCU']
 df126 = df126.loc[(df126['Source'] == top9) & (df126['Opening Speed'] == t9_speed)]
 df126['预警时间'] = df126['预警时间'].str.slice(0,10)
 df126= pd.DataFrame(df126.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df126 = df126.sort_values(by=['预警时间'])
 ax = df126.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df126.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df126['Opening Time Count']))), math.ceil(max(list(df126['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top9 +' '+ 'Opening Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top9 Opening Time Trend')
    plt.close()


#Top 10 No. of Opening Time Trend (Original) --> df127
try:
 top10 = df115.iloc[9]['Source']
 t10_speed= df115.iloc[9]['Opening Speed']
 df127 = df56.copy()
 df127['车厢'] = df127['车厢'].astype(str).str.zfill(2)
 df127['Source'] = df127['车组']+ '_' + df127['车厢'] + '_' + df127['Opening DCU']
 df127 = df127.loc[(df127['Source'] == top10) & (df127['Opening Speed'] == t10_speed)]
 df127['预警时间'] = df127['预警时间'].str.slice(0,10)
 df127= pd.DataFrame(df127.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df127 = df127.sort_values(by=['预警时间'])
 ax = df127.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df127.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df127['Opening Time Count']))), math.ceil(max(list(df127['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top10 +' '+ 'Opening Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top10 Opening Time Trend')
    plt.close()


# Top Ten Opening Time Trend Graphs (Group by Source & Occurring Time)  -->  
try:
    df404 = pd.DataFrame(pd.concat([df118,df119,df120,df121,df122,df123,df124,df125,df126,df127],axis = 0)) 
    df404 = df404.reset_index()

except:
    print('No Top Ten Opeing Time Trend')
    pass


# In[1]:

# Change datetime to date (Formatting)
StartDate = StartDate.date()
EndDate = EndDate.date()

# Create a a dashboard for Opening Time Alarm


try:
# fig --> Top Ten Opening Speed Distribution Graph

    fig = px.bar(df115,x='Source',
                y='Opening Time Count',
                title = f'Top Ten Opening Speed Graph',
                color = 'Opening Speed',
                hover_name = 'Source')

# fig1 --> Opening Speed Distribution Graph

    fig1 = px.bar(df400,
                  x='Opening Speed',
                  y='Opening Time Count',
                  title =f'Opening Time Speed Distribution (Normal)',
                hover_name = 'Opening Speed')    

# fig2 --> Opening Speed Distribution Graph (Range)

    fig2 = px.bar(df168,
              x= 'Speed_Range',
              y = 'Opening_Range_Count',
              title = f'Opening_Time_Distribution (Range)',
              hover_name = 'Speed_Range')   

# fig3 --> Closing Speed Distribution Graph (All)

    fig3 = px.bar(df114,
              x='Source',
              y='Opening Time Count',
              title =f'Opening Time Distribution (All)',
              hover_name = 'Source',
              color = 'Opening Speed',
              hover_data =['Opening Speed','Opening Time Count'])      
             
# Get the Highest Rank of Opening Speed Distribution (All)

    #op_all_max = df114.nlargest(n=1,columns=['Opening Time Count'])
    #op_all_max = op_all_max.iloc[0]['Source']

  

    layout = html.Div([
     html.Div([html.Header(f"Opening Time ({StartDate} to {EndDate})"),
     html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
     dcc.RadioItems(
                    id='radio_new_op',
                    options=[
                             {'label': 'Select All', 'value': 'op_slt_all'},
                             {'label': 'Single', 'value': 'op_single'},
                    ],
                    value='op_single',
                    inline = True,
                    style={"width": "60%"}
                ), 
     html.Div(id = 'new_op_container',children=[ 
     #html.Label([f'The Highest Opening Time DCU : {op_all_max}'], style = {'font-size' : 18}),
     html.Div([
            dcc.Graph(id = 'all_new_op',figure = fig3)],className = 'twelve columns'),],style = {'display':'none'}),

     html.Div(id='mydropdown-container1', children=[ 
     dcc.Dropdown(id="mydropdown",
                  options = sorted(df403['Opening Speed'].unique()),
                  value = df403.iloc[0]['Opening Speed']),  
     html.Div([

            dcc.Graph(id = 'op_distri')],className= 'twelve columns'),],style = {'display':'block'}),
        html.Div([
            html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                    id='radio_op',
                    options=[
                             {'label': 'All', 'value': 'op_all'},
                             {'label': 'Range', 'value': 'op_range'},
                    ],
                    value='op_all',
                    inline = True,
                    style={"width": "60%"}
                ),            
            dcc.Graph(id ='all_op_distri')],className ='twelve columns'),],className='row'),     
        html.Div([html.H2("Data", style={"textAlign":"center"}),
        html.Hr(),
        html.Div(id='table_container_all1',children =[
                    html.Div(dash_table.DataTable(df60.to_dict('records'), [{"name": i, "id": i} for i in df60.columns],
                          editable = False,
                          filter_action = 'native',
                          sort_action = 'native',
                          sort_mode='multi',
                          page_action= 'native',
                          page_current = 0,
                          page_size = 10,                      
                          style_cell_conditional=[                              
                                       {'if': {'column_id': c},
                                        'textAlign': 'center'    
                                       } for c in ['Source','预警时间 (Opening)']
                                
                          ],
                          style_data={
                                'color': 'white',
                                'backgroundColor': 'rgb(50, 50, 50)'
                          }, 
                          style_header={
                                'backgroundColor': 'rgb(30, 30, 30)',
                                'color': 'white',
                                'fontWeight': 'bold'
                                } ))],className = 'twelve columns'),
        html.Div(id='table_container_single1',children =[
        html.Div(id='table',children = 'Excel')]),],className='row'),
        html.H2("Trend", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([
            dcc.Dropdown(id="mydropdown2",
                          options = df404['Source'].unique(),
                          value = df404.iloc[0]['Source']),
            dcc.Graph(id = 'top_ten_trends')],className ='five columns'),
        html.Div([dcc.Graph(id='top_ten_opening',figure = fig)],className = 'five columns'),
        ])



    @app.callback(
        Output('new_op_container','style'),
        Output('mydropdown-container1','style'),
        Input('radio_new_op','value')

    )

    def show_hide_all(visibility_state):
        if visibility_state == 'op_slt_all':
            return {'display':'block'} , {'display' : 'none'}
        else:
            return {'display':'none'} , {'display' : 'block'}
 
        raise PreventUpdate


    @app.callback(
        Output('table_container_all1','style'),
        Output('table_container_single1','style'),
        Input('radio_new_op','value')
    )


    def show_hide_table(visibility_state):
        if visibility_state == 'op_slt_all':
            return {'display':'block'} , {'display' : 'none'}
        if visibility_state == 'op_single':
            return {'display':'none'}, {'display' : 'block'}
    
        raise PreventUpdate

    @app.callback(
        Output('op_distri', 'figure'),
        Output('table','children'),
        Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df114.loc[df114['Opening Speed']==changes]
        filtered_data2 = df60.loc[df60['Opening Speed']==changes]

        fig_op_dis = px.bar(filtered_data,
                     x='Source',
                     y='Opening Time Count',
                     title =f'Opening Time Distribution (Filter)',
                     hover_name = 'Source',
                     hover_data =['Opening Speed','Opening Time Count'])
    
        filtered_data2 = filtered_data2.drop(columns=['Speed_Range'], axis = 1)
    
        tb = html.Div([dash_table.DataTable(filtered_data2.to_dict('records'), [{"name": i, "id": i} for i in filtered_data2.columns],
                          editable = False,
                          filter_action = 'native',
                          sort_action = 'native',
                          sort_mode='multi',
                          page_action= 'native',
                          page_current = 0,
                          page_size = 10,                      
                          style_cell_conditional=[                              
                                       {'if': {'column_id': c},
                                        'textAlign': 'center'    
                                       } for c in ['Source','预警时间 (Opening)']
                                
                          ],
                          style_data={
                                'color': 'white',
                                'backgroundColor': 'rgb(50, 50, 50)'
                          }, 
                          style_header={
                                'backgroundColor': 'rgb(30, 30, 30)',
                                'color': 'white',
                                'fontWeight': 'bold'
                                } )],className='twelve columns'),
    

    
    
    
        return fig_op_dis , tb


    @app.callback(
        Output('all_op_distri','figure'),
        Input('radio_op','value')
    )


    def op_dis_input(values):
        if values == 'op_all':
            return fig1
        if values == 'op_range':
            return fig2




    @app.callback(
        Output('top_ten_trends','figure'),
        Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df404.loc[df404['Source']==changes]
    
    
        fig_top_trend = px.line(fil_data,
                            x='预警时间',
                            y='Opening Time Count',
                            title = f'Top Ten Trend Graphs',
                            hover_name = 'Source',
                            markers = True
                            )
        return fig_top_trend

except:
    print('No Opening Time Dashboard')

# In[ ]:




