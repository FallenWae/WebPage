
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
from load_data import get_dataframe , map_id, map_stname, user, opening_range
from dash import Dash, dcc, html, Input, Output, dash_table
from dash.exceptions import PreventUpdate

df6 = get_dataframe()

# Closing Speed Alarm --> df57
df57 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df57['Current_Station_Closing'] = df57['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df57 = df57.dropna(axis = 0, how='any')
df57['Current_Station_Closing'] = df57['Current_Station_Closing'].astype("int")
df57['Closing DCU'] = df57['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Door Closing)')
df57['Closing Speed'] = df57['预警描述'].str.extract('(?:.*Door Closing Time)([0.0-9.0]+)')
df57['Closing Speed'] = df57['Closing Speed'].astype("float")
df57 = df57.drop(columns = '预警描述',axis = 1)
df57 = df57.reindex(columns=['车组','车厢','预警时间','Current_Station_Closing','Closing DCU','Closing Speed'])
df57 = df57.dropna(axis = 0 ,how = 'any')
df57 = df57.reset_index(drop=True)

# Closing Time Count in Range  (Group --> 3.0-3.9 , 4.0-4.9 ......  )
try:
    df169 = df57.copy()
    df169 = df169.drop(df169[df169['Closing Speed'] < 3.7].index, axis = 'rows')
    df169['Speed_Range'] = df169['Closing Speed'].apply(lambda op_range : opening_range(op_range))
    df169 = pd.DataFrame(df169.groupby(['Speed_Range']).size(),columns=['Closing_Range_Count']).reset_index()
    df169['sortout'] = df169['Speed_Range'].str.extract('(?:.*-)([0.0-9.0]+)(?:.9)')
    df169['sortout'] = df169['sortout'].astype('int')
    df169 = df169.sort_values(by='sortout',ascending = True)
    df169.plot.barh(x='Speed_Range',y = 'Closing_Range_Count', rot=0, width = 0.7,figsize = (12,12))
    plt.title('Closing_Time_Distribution (Range)')
    plt.ylabel('Closing Speed Range')
    plt.xlabel('Count')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Closing_Time_Distribution (Range).png')
    plt.close()
    
except:
    plt.close()
    print('No Closing Time Count (Range)')

# Closing Time Criteria  -->  df62
df62 = df6.copy()
df62['Hi'] = df62['预警描述'].str.extract('(?:.*>)([0.0-9.0]+)(?:)')
df62 = df62.drop(df62[df62['Hi'] == '0'].index, axis = 'rows')
df62 = df62.dropna(axis=0,how='any')
df62.loc[(df62['预警描述'].str.contains('Door Closing Time') == True),'Closing Standard'] = '> ' + df62['Hi']
df62 = df62.dropna(axis = 0, how = 'any')
df62 = pd.DataFrame(df62['Closing Standard'])[:1]
df62 = df62.reset_index(drop = True)

# Closing Time Excel Files in Dashboard
df59 = df57.copy()
df59 = pd.DataFrame(df59.groupby(['Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
df63 = pd.DataFrame(pd.concat([df57,df62],axis=1))
df63 = df63.set_axis(['车组 (Closing)','车厢 (Closing)','预警时间 (Closing)','Current_Station_Closing','Closing DCU','Closing Speed','Closing Standard'], axis= 'columns')
df63['车厢 (Closing)'] = df63['车厢 (Closing)'].astype(str).str.zfill(2)
df63 = df63.drop(df63[df63['Closing Speed'] < 3.6].index, axis = 'rows')
df63['Source'] = df63['车组 (Closing)']+ '_' + df63['车厢 (Closing)'] + '_' + df63['Closing DCU']
df63['Platform ID'] = df63['Current_Station_Closing'].apply(lambda idxx : map_id(idxx))
df63["Current_Station_Closing"]= df63["Current_Station_Closing"].apply(lambda name : map_stname(name))
df63['Speed_Range'] = df63['Closing Speed'].apply(lambda op_range : opening_range(op_range))
df63['sort1']= df63['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df63['sort2']= df63['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
df63['sort3']= df63['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
df63['sort1'] = df63['sort1'].astype("int")
df63['sort2'] = df63['sort2'].astype("int")
df63['sort3'] = df63['sort3'].astype("int")
df63 = df63.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = True)
df63 = df63.fillna('               // ')
df63 = df63.dropna(axis = 0 ,how = 'any')
df63 = df63.reindex(columns=['Source','预警时间 (Closing)','Current_Station_Closing','Platform ID','Closing Speed','Speed_Range','Closing Standard'])
    

# Drop Closing Speed if less than 3.6 
df405 = df59.drop(df59[df59['Closing Speed'] < 3.6].index, axis = 'rows')
df405['Closing Speed'] = df405['Closing Speed'].astype('str')

# Selector of Closing Time (For DropDownList [Trainset])  -->  df116
# Top Ten Closing Time Alarm Graph in Dashboard  -->  df117
df153 = df57.copy()
df153 = df153.drop(df153[df153['Closing Speed'] < 3.5].index, axis = 'rows')
df116 = df153.copy()
# Top Ten DCU Closing Time Excel File (Original)--> df116 
try:
    df116['车厢'] = df116['车厢'].astype(str).str.zfill(2)
    df116['Source'] = df116['车组']+ '_' + df116['车厢'] + '_' + df116['Closing DCU']
    df116['预警时间'] = df116['预警时间'].str.slice(0,10)
    df116 = pd.DataFrame(df116.groupby(['Source','Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
    df116 = df116.reindex(columns=['Source','Closing Speed','Closing Time Count'])
    df116['sort1']= df116['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df116['sort2']= df116['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df116['sort3']= df116['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df116['sort1'] = df116['sort1'].astype("int")
    df116['sort2'] = df116['sort2'].astype("int")
    df116['sort3'] = df116['sort3'].astype("int")
    df116 = df116.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = True)
    df117 = df116.nlargest(n = 10 , columns =['Closing Time Count'])
    df117 = df117.sort_values(by='Closing Time Count',ignore_index = True, ascending = False)

except:
    print('No Top Ten DCU Closing Time Result')

# For sorting the dropdownlist (3.8 --> 25.4)
df406 = pd.DataFrame(df63['Closing Speed'])
df406 = df406.sort_values(by=['Closing Speed'])

#Top 1 No. of Closing Time Trend (Original) --> df128
try:
 top1 = df117.iloc[0]['Source']
 t1_speed= df117.iloc[0]['Closing Speed']
 df128 = df57.copy()
 df128['车厢'] = df128['车厢'].astype(str).str.zfill(2)
 df128['Source'] = df128['车组']+ '_' + df128['车厢'] + '_' + df128['Closing DCU']
 df128 = df128.loc[(df128['Source'] == top1) & (df128['Closing Speed'] == t1_speed)]
 df128['预警时间'] = df128['预警时间'].str.slice(0,10)
 df128= pd.DataFrame(df128.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df128 = df128.sort_values(by=['预警时间'])
 ax = df128.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df128.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df128['Closing Time Count']))), math.ceil(max(list(df128['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top1 +' '+ 'Closing Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top1 Closing Time Trend')
    plt.close()

#Top 2 No. of Closing Time Trend (Original) --> df129
try:
 top2 = df117.iloc[1]['Source']
 t2_speed= df117.iloc[1]['Closing Speed']
 df129 = df57.copy()
 df129['车厢'] = df129['车厢'].astype(str).str.zfill(2)
 df129['Source'] = df129['车组']+ '_' + df129['车厢'] + '_' + df129['Closing DCU']
 df129 = df129.loc[(df129['Source'] == top2) & (df129['Closing Speed'] == t2_speed)]
 df129['预警时间'] = df129['预警时间'].str.slice(0,10)
 df129= pd.DataFrame(df129.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df129 = df129.sort_values(by=['预警时间'])
 ax = df129.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df129.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df129['Closing Time Count']))), math.ceil(max(list(df129['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top2 +' '+ 'Closing Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top2 Closing Time Trend')
    plt.close()


#Top 3 No. of Closing Time Trend (Original) --> df130

try:
 top3 = df117.iloc[2]['Source']
 t3_speed= df117.iloc[2]['Closing Speed']
 df130 = df57.copy()
 df130['车厢'] = df130['车厢'].astype(str).str.zfill(2)
 df130['Source'] = df130['车组']+ '_' + df130['车厢'] + '_' + df130['Closing DCU']
 df130 = df130.loc[(df130['Source'] == top3) & (df130['Closing Speed'] == t3_speed)]
 df130['预警时间'] = df130['预警时间'].str.slice(0,10)
 df130= pd.DataFrame(df130.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df130 = df130.sort_values(by=['预警时间'])
 ax = df130.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df130.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df130['Closing Time Count']))), math.ceil(max(list(df130['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top3 +' '+ 'Closing Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top3 Closing Time Trend')
    plt.close()


#Top 4 No. of Closing Time Trend (Original) --> df131

try:
 top4 = df117.iloc[3]['Source']
 t4_speed= df117.iloc[3]['Closing Speed']
 df131 = df57.copy()
 df131['车厢'] = df131['车厢'].astype(str).str.zfill(2)
 df131['Source'] = df131['车组']+ '_' + df131['车厢'] + '_' + df131['Closing DCU']
 df131 = df131.loc[(df131['Source'] == top4) & (df131['Closing Speed'] == t4_speed)]
 df131['预警时间'] = df131['预警时间'].str.slice(0,10)
 df131= pd.DataFrame(df131.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df131 = df131.sort_values(by=['预警时间'])
 ax = df131.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df131.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df131['Closing Time Count']))), math.ceil(max(list(df131['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top4 +' '+ 'Closing Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top4 Closing Time Trend')
    plt.close()


#Top 5 No. of Closing Time Trend (Original) --> df132

try:
 top5 = df117.iloc[4]['Source']
 t5_speed= df117.iloc[4]['Closing Speed']
 df132 = df57.copy()
 df132['车厢'] = df132['车厢'].astype(str).str.zfill(2)
 df132['Source'] = df132['车组']+ '_' + df132['车厢'] + '_' + df132['Closing DCU']
 df132 = df132.loc[(df132['Source'] == top5) & (df132['Closing Speed'] == t5_speed)]
 df132['预警时间'] = df132['预警时间'].str.slice(0,10)
 df132= pd.DataFrame(df132.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df132 = df132.sort_values(by=['预警时间'])
 ax = df132.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df132.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df132['Closing Time Count']))), math.ceil(max(list(df132['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top5 +' '+ 'Closing Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top5 Closing Time Trend')
    plt.close()


#Top 6 No. of Closing Time Trend (Original) --> df133

try:
 top6 = df117.iloc[5]['Source']
 t6_speed= df117.iloc[5]['Closing Speed']
 df133 = df57.copy()
 df133['车厢'] = df133['车厢'].astype(str).str.zfill(2)
 df133['Source'] = df133['车组']+ '_' + df133['车厢'] + '_' + df133['Closing DCU']
 df133 = df133.loc[(df133['Source'] == top6) & (df133['Closing Speed'] == t6_speed)]
 df133['预警时间'] = df133['预警时间'].str.slice(0,10)
 df133= pd.DataFrame(df133.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df133 = df133.sort_values(by=['预警时间'])
 ax = df133.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df133.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df133['Closing Time Count']))), math.ceil(max(list(df133['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top6 +' '+ 'Closing Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top6 Closing Time Trend')
    plt.close()


#Top 7 No. of Closing Time Trend (Original) --> df134

try:
 top7 = df117.iloc[6]['Source']
 t7_speed= df117.iloc[6]['Closing Speed']
 df134 = df57.copy()
 df134['车厢'] = df134['车厢'].astype(str).str.zfill(2)
 df134['Source'] = df134['车组']+ '_' + df134['车厢'] + '_' + df134['Closing DCU']
 df134 = df134.loc[(df134['Source'] == top7) & (df134['Closing Speed'] == t7_speed)]
 df134['预警时间'] = df134['预警时间'].str.slice(0,10)
 df134= pd.DataFrame(df134.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df134 = df134.sort_values(by=['预警时间'])
 ax = df134.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df134.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df134['Closing Time Count']))), math.ceil(max(list(df134['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top7 +' '+ 'Closing Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top7 Closing Time Trend')
    plt.close()


#Top 8 No. of Closing Time Trend (Original) --> df135

try:
 top8 = df117.iloc[7]['Source']
 t8_speed= df117.iloc[7]['Closing Speed']
 df135 = df57.copy()
 df135['车厢'] = df135['车厢'].astype(str).str.zfill(2)
 df135['Source'] = df135['车组']+ '_' + df135['车厢'] + '_' + df135['Closing DCU']
 df135 = df135.loc[(df135['Source'] == top8) & (df135['Closing Speed'] == t8_speed)]
 df135['预警时间'] = df135['预警时间'].str.slice(0,10)
 df135= pd.DataFrame(df135.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df135 = df135.sort_values(by=['预警时间'])
 ax = df135.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df135.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df135['Closing Time Count']))), math.ceil(max(list(df135['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top8 +' '+ 'Closing Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top8 Closing Time Trend')
    plt.close()


#Top 9 No. of Closing Time Trend (Original) --> df136

try:
 top9 = df117.iloc[8]['Source']
 t9_speed= df117.iloc[8]['Closing Speed']
 df136 = df57.copy()
 df136['车厢'] = df136['车厢'].astype(str).str.zfill(2)
 df136['Source'] = df136['车组']+ '_' + df136['车厢'] + '_' + df136['Closing DCU']
 df136 = df136.loc[(df136['Source'] == top9) & (df136['Closing Speed'] == t9_speed)]
 df136['预警时间'] = df136['预警时间'].str.slice(0,10)
 df136= pd.DataFrame(df136.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df136 = df136.sort_values(by=['预警时间'])
 ax = df136.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df136.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df136['Closing Time Count']))), math.ceil(max(list(df136['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top9 +' '+ 'Closing Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top9 Closing Time Trend')
    plt.close()


#Top 10 No. of Closing Time Trend (Original) --> df137

try:
 top10 = df117.iloc[9]['Source']
 t10_speed= df117.iloc[9]['Closing Speed']
 df137 = df57.copy()
 df137['车厢'] = df137['车厢'].astype(str).str.zfill(2)
 df137['Source'] = df137['车组']+ '_' + df137['车厢'] + '_' + df137['Closing DCU']
 df137 = df137.loc[(df137['Source'] == top10) & (df137['Closing Speed'] == t10_speed)]
 df137['预警时间'] = df137['预警时间'].str.slice(0,10)
 df137= pd.DataFrame(df137.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df137 = df137.sort_values(by=['预警时间'])
 ax = df137.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df137.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df137['Closing Time Count']))), math.ceil(max(list(df137['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top10 +' '+ 'Closing Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 plt.close()
    
except:
    print('No Top10 Closing Time Trend')
    plt.close()

# Top Ten Closing Time Trend Graphs (Group by Source & Occurring Time)  -->  df407
try:
    df407 = pd.DataFrame(pd.concat([df128,df129,df130,df131,df132,df133,df134,df135,df136,df137],axis = 0))
    df407 = df407.reset_index()

except:
    print('No Top Ten Closing Time Trend')

# Create a a dashboard for Closing Time Alarm

# fig --> Top Ten Closing Speed Distribution Graph
try:
    fig = px.bar(df117,x = 'Source',
            y = 'Closing Time Count',
            title = f'Top Ten Closing Speed Graph',
            color = 'Closing Speed',
            hover_name = 'Source')

# fig1 --> Closing Speed Distribution Graph (Single)

    fig1 = px.bar(df405,
              x = 'Closing Speed',
              y = 'Closing Time Count',
              title = f'Closing Time Speed Distribution (Normal)',
              hover_name = 'Closing Speed')             
             
# fig2 --> Closing Speed Distribution Graph (Range)

    fig2 = px.bar(df169,
              x = 'Speed_Range',
              y = 'Closing_Range_Count',
              title = f'Closing_Time_Distribution (Range)',
              hover_name = 'Speed_Range')

# fig3 --> Closing Speed Distribution Graph (All)

    fig3 = px.bar(df116,
              x = 'Source',
              y = 'Closing Time Count',
              title = f'Closing Time Distribution (All)',
              hover_name = 'Source',
              color = 'Closing Speed',
              hover_data = ['Closing Speed','Closing Time Count'])


# Get the Highest Rank of Closing Speed Distribution (All)

    #cl_all_max = df116.nlargest(n=1,columns=['Closing Time Count'])
    #cl_all_max = cl_all_max.iloc[0]['Source']


    layout = html.Div([
        html.Div([html.Header("Closing Time"),
        html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
        dcc.RadioItems(
                    id='radio_new_cl',
                    options=[
                             {'label': 'Select All', 'value': 'cl_slt_all'},
                             {'label': 'Single', 'value': 'cl_single'},
                    ],
                    value='cl_single',
                    inline = True,
                    style={"width": "60%"}
                ),
        html.Div(id = 'new_cl_container',children=[ 
        #html.Label([f'The Highest Closing Time DCU : {cl_all_max}'], style = {'font-size' : 18}),
        html.Div([
            dcc.Graph(id = 'all_new_cl',figure = fig3)],className = 'twelve columns'),],style = {'display':'none'}),

        html.Div(id='mydropdown-container', children=[    
                    dcc.Dropdown(id="mydropdown",
                        options = sorted(df406['Closing Speed'].unique()),
                        value = df406.iloc[0]['Closing Speed']),
        html.Div([

            dcc.Graph(id = 'cl_distri')],className= 'twelve columns'),],style = {'display':'block'}),
        html.Div([
            html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                    id='radio_cl',
                    options=[
                             {'label': 'All', 'value': 'cl_all'},
                             {'label': 'Range', 'value': 'cl_range'},
                    ],
                    value='cl_all',
                    inline = True,
                    style={"width": "60%"}
                ),
            dcc.Graph(id ='all_cl_distri')],className ='twelve columns'),],className='row'),     
        html.Div([html.H2("Data", style={"textAlign":"center"}),
        html.Hr(),
        html.Div(id='table_container_all',children =[
                    html.Div(dash_table.DataTable(df63.to_dict('records'), [{"name": i, "id": i} for i in df63.columns],
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
                                       } for c in ['Source','预警时间 (Closing)']
                                
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

        html.Div(id='table_container_single',children =[                        
            html.Div(id='table3',children = 'Excel')]),],className='row'),

        html.H2("Trend", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([
            dcc.Dropdown(id="mydropdown2",
                        options = df407['Source'].unique(),
                        value = df407.iloc[0]['Source']),
            dcc.Graph(id = 'top_ten_trends1')],className ='five columns'),
        html.Div([dcc.Graph(id='top_ten_closing',figure = fig)],className = 'five columns'),
        ])


    @app.callback(
        Output('new_cl_container','style'),
        Output('mydropdown-container','style'),
        Input('radio_new_cl','value')

    )

    def show_hide_all(visibility_state):
        if visibility_state == 'cl_slt_all':
            return {'display':'block'} , {'display' : 'none'}
        else:
            return {'display':'none'} , {'display' : 'block'}
 
        raise PreventUpdate


    @app.callback(
        Output('table_container_all','style'),
        Output('table_container_single','style'),
        Input('radio_new_cl','value')
    )


    
    def show_hide_table(visibility_state):
        if visibility_state == 'cl_slt_all':
            return {'display':'block'} , {'display' : 'none'}
        if visibility_state == 'cl_single':
            return {'display':'none'}, {'display' : 'block'}
    
        raise PreventUpdate

    @app.callback(
        Output('cl_distri', 'figure'),
        Output('table3','children'),
        Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df116.loc[df116['Closing Speed']==changes]
        filtered_data2 = df63.loc[df63['Closing Speed']==changes]
        #a = filtered_data2.nlargest(n=1,columns=['Obstacle Detected Count'])
        #a = a.iloc[0]['Source']
        #print(a)
    
        fig_cl_dis = px.bar(filtered_data,
                 x='Source',
                 y='Closing Time Count',
                 title =f'Closing Time Distribution (Filter)',
                 hover_name = 'Source',
                 hover_data =['Closing Speed','Closing Time Count'])
        fig_cl_dis.update_yaxes(dtick = 1)
    
        filtered_data2 = filtered_data2.drop(columns=['Speed_Range'],axis = 1)
    
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
                                       } for c in ['Source','预警时间 (Closing)']
                                
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
    

    
    
    
        return fig_cl_dis , tb


    @app.callback(
        Output('all_cl_distri','figure'),
        Input('radio_cl','value')
    )


    def op_dis_input(values):
        if values == 'cl_all':
            return fig1
        if values == 'cl_range':
            return fig2


    @app.callback(
        Output('top_ten_trends1','figure'),
        Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df407.loc[df407['Source']==changes]
    
    
        fig_top_trend = px.line(fil_data,
                            x='预警时间',
                            y='Closing Time Count',
                            title = f'Top Ten Trend Graphs',
                            hover_name = 'Source',
                            markers = True
                            )
        return fig_top_trend

except:
    print('No Closing Time Dashboard')
