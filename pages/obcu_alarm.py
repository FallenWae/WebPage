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



# OBCU Alarm (Excel File)  -->  df301
df301 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df301 = df301.loc[df301['预警描述'].str.contains('OBCU active')]
df301['Current_Station'] = df301['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df301 = df301.dropna(axis = 0, how='any')
df301['Current_Station'] = df301['Current_Station'].astype("int")
df301 = df301.reindex(columns=['车组','车厢','预警时间','Current_Station','预警描述'])
df301 = df301.dropna(axis = 0 ,how = 'any')
df301 = df301.reset_index(drop=True)



# OBCU Excel Files in Dashboard -->  df806 , df807
df806 = df301.copy()
df806 = pd.DataFrame(df806.groupby(['车组']).size(),columns=['OBCU Count']).reset_index()
df806['sort1'] = df806['车组'].str.extract('(?:.*T)([0-9]+)')
df806['sort1'] = df806['sort1'].astype('int')
df806 = df806.sort_values(by=['sort1'], ignore_index = True , ascending = True)
#df184['Pressure Fall'] = df184['Pressure Fall'].astype('str')
df807 = df301.copy()
df807['车厢'] = df807['车厢'].astype(str).str.zfill(2)
df807['Source'] = df807['车组']+ '_' + df807['车厢']
df807['Platform ID'] = df807['Current_Station'].apply(lambda idxx : map_id(idxx))
df807["Current_Station"]= df807["Current_Station"].apply(lambda name : map_stname(name))
df807['Type'] = df807['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df807['Type'] = 'T' + df807['Type']
df807['sort1']= df807['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df807['sort2']= df807['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df807['sort1'] = df807['sort1'].astype("int")
df807['sort2'] = df807['sort2'].astype("int")
df807 = df807.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df807 = df807.fillna('               // ')
df807 = df807.dropna(axis = 0 ,how = 'any')
df807 = df807.reindex(columns=['Source','预警时间','Current_Station','Platform ID','Type'])



# OBCU Excel File (Group Count)   -->  df808 , df809

df808 = df807.copy()
df808 = pd.DataFrame(df808.groupby(['Source']).size(),columns=['OBCU Count']).reset_index()
df808 = df808.reindex(columns=['Source','OBCU Count'])
df808 = df808.sort_values(by='OBCU Count',ascending = False)
df808['Type'] = df808['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df808['Type'] = 'T' + df808['Type']
df808['sort1']= df808['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df808['sort2']= df808['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df808['sort1'] = df808['sort1'].astype("int")
df808['sort2'] = df808['sort2'].astype("int")
df808 = df808.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df809 = df808.nlargest(n = 10 , columns =['OBCU Count'])



# Selector of OBCU Alarm (For DropDownList [Trainset])  -->  df810
df810 = df807.copy()
df810['sort1']= df810['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df810['sort2']= df810['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df810['sort1'] = df810['sort1'].astype("int")
df810['sort2'] = df810['sort2'].astype("int")
df810 = df810.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)



#Top 1 No. of OBCU Alarm Trend--> df305
try:
    top1 = df809.iloc[0]['Source']
    df305 = df807.copy()
    df305 = df305.loc[(df305['Source'] == top1)]
    df305['预警时间'] = df305['预警时间'].str.slice(0,10)
    df305= pd.DataFrame(df305.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df305 = df305.sort_values(by=['预警时间'])
    ax = df305.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df305.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top1 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top1 OBCU Trend')
    plt.close()



#Top 2 No. of OBCU Alarm Trend--> df306
try:
    top2 = df809.iloc[1]['Source']
    df306 = df807.copy()
    df306 = df306.loc[(df306['Source'] == top2)]
    df306['预警时间'] = df306['预警时间'].str.slice(0,10)
    df306= pd.DataFrame(df306.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df306 = df306.sort_values(by=['预警时间'])
    ax = df306.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df306.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top2 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top2 OBCU Trend')
    plt.close()



#Top 3 No. of OBCU Alarm Trend--> df307
try:
    top3 = df809.iloc[2]['Source']
    df307 = df807.copy()
    df307 = df307.loc[(df307['Source'] == top3)]
    df307['预警时间'] = df307['预警时间'].str.slice(0,10)
    df307= pd.DataFrame(df307.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df307 = df307.sort_values(by=['预警时间'])
    ax = df307.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df307.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top3 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top3 OBCU Trend')
    plt.close()



#Top 4 No. of OBCU Alarm Trend--> df308
try:
    top4 = df809.iloc[3]['Source']
    df308 = df807.copy()
    df308 = df308.loc[(df308['Source'] == top4)]
    df308['预警时间'] = df308['预警时间'].str.slice(0,10)
    df308= pd.DataFrame(df308.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df308 = df308.sort_values(by=['预警时间'])
    ax = df308.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df308.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top4 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top4 OBCU Trend')
    plt.close()



#Top 5 No. of OBCU Alarm Trend--> df309
try:
    top5 = df809.iloc[4]['Source']
    df309 = df807.copy()
    df309 = df309.loc[(df309['Source'] == top5)]
    df309['预警时间'] = df309['预警时间'].str.slice(0,10)
    df309= pd.DataFrame(df309.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df309 = df309.sort_values(by=['预警时间'])
    ax = df309.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df309.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top5 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top5 OBCU Trend')
    plt.close()



#Top 6 No. of OBCU Alarm Trend--> df310
try:
    top6 = df809.iloc[5]['Source']
    df310 = df807.copy()
    df310 = df310.loc[(df310['Source'] == top6)]
    df310['预警时间'] = df310['预警时间'].str.slice(0,10)
    df310= pd.DataFrame(df310.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df310 = df310.sort_values(by=['预警时间'])
    ax = df310.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df310.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top6 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top6 OBCU Trend')
    plt.close()



#Top 7 No. of OBCU Alarm Trend--> df311
try:
    top7 = df809.iloc[6]['Source']
    df311 = df807.copy()
    df311 = df311.loc[(df311['Source'] == top7)]
    df311['预警时间'] = df311['预警时间'].str.slice(0,10)
    df311= pd.DataFrame(df311.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df311 = df311.sort_values(by=['预警时间'])
    ax = df311.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df311.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top7 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top7 OBCU Trend')
    plt.close()



#Top 8 No. of OBCU Alarm Trend--> df312
try:
    top8 = df809.iloc[7]['Source']
    df312 = df807.copy()
    df312 = df312.loc[(df312['Source'] == top8)]
    df312['预警时间'] = df312['预警时间'].str.slice(0,10)
    df312= pd.DataFrame(df312.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df312 = df312.sort_values(by=['预警时间'])
    ax = df312.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df312.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top8 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top8 OBCU Trend')
    plt.close()



#Top 9 No. of OBCU Alarm Trend--> df313
try:
    top9 = df809.iloc[8]['Source']
    df313 = df807.copy()
    df313 = df313.loc[(df313['Source'] == top9)]
    df313['预警时间'] = df313['预警时间'].str.slice(0,10)
    df313= pd.DataFrame(df313.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df313 = df313.sort_values(by=['预警时间'])
    ax = df313.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df313.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top9 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top9 OBCU Trend')
    plt.close()



#Top 10 No. of OBCU Alarm Trend--> df314
try:
    top10 = df809.iloc[9]['Source']
    df314 = df807.copy()
    df314 = df314.loc[(df314['Source'] == top10)]
    df314['预警时间'] = df314['预警时间'].str.slice(0,10)
    df314= pd.DataFrame(df314.groupby(['Source' ,'预警时间']).size(),columns=['OBCU Count']).reset_index()
    df314 = df314.sort_values(by=['预警时间'])
    ax = df314.plot.scatter(x= '预警时间', y= 'OBCU Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df314.plot.line(x= '预警时间', y='OBCU Count', ax=ax, style='b',rot=25)
    plt.title(top10 +' '+ 'OBCU Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.close()
    
except:
    print('No Top10 OBCU Trend')
    plt.close()


# Top Ten OBCU Trend Graphs (Group by Source & Occurring Time)  -->  df811

try:
    df811 = pd.concat([df305,df306,df307,df308,df309,df310,df311,df312,df313,df314], axis = 0)
except:
    print('No Top Ten OBCU Result to Concatenate')


# Change datetime to date (Formatting)
StartDate = StartDate.date()
EndDate = EndDate.date()


# Create a dashborad for OBCU Alarm
try:

# fig --> All Trainset OBCU Group Count Graph


    fig = px.bar(df806,x='车组',
             y='OBCU Count',
             title = f'All Trainset OBCU Group Count',
             hover_name='车组')

# fig1 --> All Top Ten OBCU Trend Graph

    fig1 = px.bar(df809,x='Source',
              y='OBCU Count',
              title = f'Top Ten OBCU Trend',
              hover_name='Source')


    layout = html.Div([
            html.Div([html.Header(f"OBCU Alarm ({StartDate} to {EndDate})"),
            html.Div([dcc.Dropdown(id="mydropdown",
                 options = df810['Type'].unique(),
                 value = df810.iloc[0]['Type']),
                 dcc.Graph(id = 'all_graphs2')],className ='six columns'),
            html.Div([
                dcc.Graph(id = 'one_graph',figure = fig)],className= 'five columns'),],className = 'row'),
            html.Div([html.H2("Data", style={"textAlign":"center"}),
            html.Hr(),
            html.Div(id='table7',children = 'Excel'),],className='row'),
            html.H2("Trend", style={"textAlign":"center"}),
            html.Hr(),
            html.Div([dcc.Dropdown(id="mydropdown2",
                options = df809['Source'].unique(),
                value = df809.iloc[0]['Source'],
                ),
            dcc.Graph(id = 'trend_graphs2')],className ='six columns'),
            html.Div([
                dcc.Graph(id = 'top_ten_trend',figure = fig1)],className ='five columns'),
        
            ])
    
   

    @app.callback(
        Output('all_graphs2','figure'),
        Output('table7', 'children'),
        Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df807.loc[df807['Type']==changes]
        filtered_data2 = df808.loc[df808['Type']==changes]
        a = filtered_data2.nlargest(n=1,columns=['OBCU Count'])
        a = a.iloc[0]['Source']
        fig_bar = px.bar(filtered_data2,
                x='Source',
                y='OBCU Count',
                title =f'The Highest OBCU Alarm Train : {a}',
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
       Output('trend_graphs2','figure'),
       Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df811.loc[df811['Source']==changes]

        fig_top_trends = px.line(fil_data.loc[fil_data['Source']==changes],
                x='预警时间',
                y='OBCU Count',
                title =f'OBCU Trend',
                hover_name = 'Source',
                markers = True)
    
        return fig_top_trends


except:
    print('No OBCU Dashboard')
