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
from load_data import get_dataframe , map_id, map_stname, user, StartDate, EndDate
from dash import Dash, dcc, html, Input, Output, dash_table

df6 = get_dataframe()


# Emergency brake Alarm (Excel File)  -->  df315
df315 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df315 = df315.loc[df315['预警描述'].str.contains('Emergency brake')]
df315['Current_Station'] = df315['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df315 = df315.dropna(axis = 0, how='any')
df315['Current_Station'] = df315['Current_Station'].astype("int")
df315 = df315.reindex(columns=['车组','车厢','预警时间','Current_Station','预警描述'])
df315 = df315.dropna(axis = 0 ,how = 'any')
df315 = df315.reset_index(drop=True)



# Emergency Brake Excel Files in Dashboard -->  df812 , df813
df812 = df315.copy()
df812 = pd.DataFrame(df812.groupby(['车组']).size(),columns=['Emergency Brake Count']).reset_index()
df812['sort1'] = df812['车组'].str.extract('(?:.*T)([0-9]+)')
df812['sort1'] = df812['sort1'].astype('int')
df812 = df812.sort_values(by=['sort1'], ignore_index = True , ascending = True)
df813 = df315.copy()
df813['车厢'] = df813['车厢'].astype(str).str.zfill(2)
df813['Source'] = df813['车组']+ '_' + df813['车厢']
df813['Platform ID'] = df813['Current_Station'].apply(lambda idxx : map_id(idxx))
df813["Current_Station"]= df813["Current_Station"].apply(lambda name : map_stname(name))
df813['Type'] = df813['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df813['Type'] = 'T' + df813['Type']
df813['sort1']= df813['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df813['sort2']= df813['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df813['sort1'] = df813['sort1'].astype("int")
df813['sort2'] = df813['sort2'].astype("int")
df813 = df813.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df813 = df813.fillna('               // ')
df813 = df813.dropna(axis = 0 ,how = 'any')
df813 = df813.reindex(columns=['Source','预警时间','Current_Station','Platform ID','Type'])



# OBCU Excel File (Group Count)   -->  df814 , df815

df814 = df813.copy()
df814 = pd.DataFrame(df814.groupby(['Source']).size(),columns=['Emergency Brake Count']).reset_index()
df814 = df814.reindex(columns=['Source','Emergency Brake Count'])
df814 = df814.sort_values(by='Emergency Brake Count',ascending = False)
df814['Type'] = df814['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df814['Type'] = 'T' + df814['Type']
df814['sort1']= df814['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df814['sort2']= df814['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df814['sort1'] = df814['sort1'].astype("int")
df814['sort2'] = df814['sort2'].astype("int")
df814 = df814.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
try:
    df815 = df814.nlargest(n = 10 , columns =['Emergency Brake Count'])
except:
    pass



# Selector of Emergency Brake Alarm (For DropDownList [Trainset])  -->  df816
df816 = df813.copy()
df816['sort1']= df816['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df816['sort2']= df816['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df816['sort1'] = df816['sort1'].astype("int")
df816['sort2'] = df816['sort2'].astype("int")
df816 = df816.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)



#Top 1 No. of Emergency Brake Alarm Trend--> df319
try:
    top1 = df815.iloc[0]['Source']
    df319 = df813.copy()
    df319 = df319.loc[(df319['Source'] == top1)]
    df319['预警时间'] = df319['预警时间'].str.slice(0,10)
    df319= pd.DataFrame(df319.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df319 = df319.sort_values(by=['预警时间'])
    ax = df319.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df319.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top1 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top1 Emergency Brake Trend')
    plt.close()



#Top 2 No. of Emergency Brake Alarm Trend--> df320
try:
    top2 = df815.iloc[1]['Source']
    df320 = df813.copy()
    df320 = df320.loc[(df320['Source'] == top2)]
    df320['预警时间'] = df320['预警时间'].str.slice(0,10)
    df320= pd.DataFrame(df320.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df320 = df320.sort_values(by=['预警时间'])
    ax = df320.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df320.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top2 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top2 Emergency Brake Trend')
    plt.close()




#Top 3 No. of Emergency Brake Alarm Trend--> df321
try:
    top3 = df815.iloc[2]['Source']
    df321 = df813.copy()
    df321 = df321.loc[(df321['Source'] == top3)]
    df321['预警时间'] = df321['预警时间'].str.slice(0,10)
    df321= pd.DataFrame(df321.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df321 = df321.sort_values(by=['预警时间'])
    ax = df321.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df321.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top3 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top3 Emergency Brake Trend')
    plt.close()



#Top 4 No. of Emergency Brake Alarm Trend--> df322
try:
    top4 = df815.iloc[3]['Source']
    df322 = df813.copy()
    df322 = df322.loc[(df322['Source'] == top4)]
    df322['预警时间'] = df322['预警时间'].str.slice(0,10)
    df322= pd.DataFrame(df322.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df322 = df322.sort_values(by=['预警时间'])
    ax = df322.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df322.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top4 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top4 Emergency Brake Trend')
    plt.close()



#Top 5 No. of Emergency Brake Alarm Trend--> df323
try:
    top5 = df815.iloc[4]['Source']
    df323 = df813.copy()
    df323 = df323.loc[(df323['Source'] == top5)]
    df323['预警时间'] = df323['预警时间'].str.slice(0,10)
    df323= pd.DataFrame(df323.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df323 = df323.sort_values(by=['预警时间'])
    ax = df323.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df323.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top5 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top5 Emergency Brake Trend')
    plt.close()



#Top 6 No. of Emergency Brake Alarm Trend--> df324
try:
    top6 = df815.iloc[5]['Source']
    df324 = df813.copy()
    df324 = df324.loc[(df324['Source'] == top6)]
    df324['预警时间'] = df324['预警时间'].str.slice(0,10)
    df324= pd.DataFrame(df324.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df324 = df324.sort_values(by=['预警时间'])
    ax = df324.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df324.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top6 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top6 Emergency Brake Trend')
    plt.close()


#Top 7 No. of Emergency Brake Alarm Trend--> df325
try:
    top7 = df815.iloc[6]['Source']
    df325 = df813.copy()
    df325 = df325.loc[(df325['Source'] == top7)]
    df325['预警时间'] = df325['预警时间'].str.slice(0,10)
    df325= pd.DataFrame(df325.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df325 = df325.sort_values(by=['预警时间'])
    ax = df325.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df325.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top7 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top7 Emergency Brake Trend')
    plt.close()



#Top 8 No. of Emergency Brake Alarm Trend--> df326
try:
    top8 = df815.iloc[7]['Source']
    df326 = df813.copy()
    df326 = df326.loc[(df326['Source'] == top8)]
    df326['预警时间'] = df326['预警时间'].str.slice(0,10)
    df326= pd.DataFrame(df326.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df326 = df326.sort_values(by=['预警时间'])
    ax = df326.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df326.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top8 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top8 Emergency Brake Trend')
    plt.close()



#Top 9 No. of Emergency Brake Alarm Trend--> df327
try:
    top9 = df815.iloc[8]['Source']
    df327 = df813.copy()
    df327 = df327.loc[(df327['Source'] == top9)]
    df327['预警时间'] = df327['预警时间'].str.slice(0,10)
    df327= pd.DataFrame(df327.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df327 = df327.sort_values(by=['预警时间'])
    ax = df327.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df327.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top9 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top9 Emergency Brake Trend')
    plt.close()



#Top 10 No. of Emergency Brake Alarm Trend--> df328
try:
    top10 = df815.iloc[9]['Source']
    df328 = df813.copy()
    df328 = df328.loc[(df328['Source'] == top10)]
    df328['预警时间'] = df328['预警时间'].str.slice(0,10)
    df328= pd.DataFrame(df328.groupby(['Source' ,'预警时间']).size(),columns=['Emergency Brake Count']).reset_index()
    df328 = df328.sort_values(by=['预警时间'])
    ax = df328.plot.scatter(x= '预警时间', y= 'Emergency Brake Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df328.plot.line(x= '预警时间', y='Emergency Brake Count', ax=ax, style='b',rot=25)
    plt.title(top10 +' '+ 'Emergency Brake Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top10 Emergency Brake Trend')
    plt.close()



# Top Ten Emergency Brake Trend Graphs (Group by Source & Occurring Time)  -->  df817
try:
    df817 = pd.concat([df319,df320,df321,df322,df323,df324,df325,df326,df327,df328], axis = 0)
except:
    print('No Top Ten Emergency Brake Result to Concatenate')


# Change datetime to date (Formatting)
StartDate = StartDate.date()
EndDate = EndDate.date()

# Create a dashborad for Emergency Brake Alarm

try:


# fig --> All Trainset Emergency Brake Group Count Graph


    fig = px.bar(df812,x='车组',
             y='Emergency Brake Count',
             title = f'All Trainset Emergency Brake Group Count',
             hover_name='车组')

# fig1 --> All Top Ten Emergency Brake Trend Graph

    fig1 = px.bar(df815,x='Source',
              y='Emergency Brake Count',
              title = f'Top Ten Emergency Brake Trend',
              hover_name='Source')



    layout = html.Div([
        html.Div([html.Header(f"Emergency Brake ({StartDate} to {EndDate})"),
        html.Div([dcc.Dropdown(id="mydropdown",
                 options = df816['Type'].unique(),
                 value = df816.iloc[0]['Type']),
        dcc.Graph(id = 'all_graphs3')],className ='six columns'),
        html.Div([
            dcc.Graph(id = 'one_graph',figure = fig)],className= 'five columns'),],className = 'row'),
        html.Div([html.H2("Data", style={"textAlign":"center"}),
        html.Hr(),
        html.Div(id='table8',children = 'Excel'),],className='row'),
        html.H2("Trend", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([dcc.Dropdown(id="mydropdown2",
              options = df815['Source'].unique(),
              value = df815.iloc[0]['Source'],
            ),
        dcc.Graph(id = 'trend_graphs3')],className ='six columns'),
        html.Div([
            dcc.Graph(id = 'top_ten_trend',figure = fig1)],className ='five columns'),
        
        ])
    
   

    @app.callback(
        Output('all_graphs3','figure'),
        Output('table8', 'children'),
        Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df813.loc[df813['Type']==changes]
        filtered_data2 = df814.loc[df814['Type']==changes]
        a = filtered_data2.nlargest(n=1,columns=['Emergency Brake Count'])
        a = a.iloc[0]['Source']
        fig_bar = px.bar(filtered_data2,
                x='Source',
                y='Emergency Brake Count',
                title =f'The Highest Emergency Brake Alarm Train : {a}',
                hover_name = 'Source')
    
        filtered_data = filtered_data.drop(columns=['Type'],axis = 1)
        tb = html.Div([dash_table.DataTable(filtered_data.to_dict('records'), [{"name": i, "id": i} for i in filtered_data.columns],
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
                                       } for c in ['Source','预警时间']
                                
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
    
    
    
    
        return fig_bar , tb

    @app.callback(
        Output('trend_graphs3','figure'),
        Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df817.loc[df817['Source']==changes]


        fig_top_trends = px.line(fil_data.loc[fil_data['Source']==changes],
                x='预警时间',
                y='Emergency Brake Count',
                title =f'Emergency Brake Trend',
                hover_name = 'Source',
                markers = True)
    
        return fig_top_trends


except:
    print('No Emergency Brake Dashboard')
