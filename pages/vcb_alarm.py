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


# VCB Alarm (Excel File)  -->  df287
df287 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df287 = df287.loc[df287['预警描述'].str.contains('VCB closed')]
df287['Current_Station'] = df287['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df287 = df287.dropna(axis = 0, how='any')
df287['Current_Station'] = df287['Current_Station'].astype("int")
df287 = df287.reindex(columns=['车组','车厢','预警时间','Current_Station','预警描述'])
df287 = df287.dropna(axis = 0 ,how = 'any')
df287 = df287.reset_index(drop=True)


# VCB Excel Files in Dashboard
df800 = df287.copy()
df800 = pd.DataFrame(df800.groupby(['车组']).size(),columns=['VCB Count']).reset_index()
df800['sort1'] = df800['车组'].str.extract('(?:.*T)([0-9]+)')
df800['sort1'] = df800['sort1'].astype('int')
df800 = df800.sort_values(by=['sort1'], ignore_index = True , ascending = True)
df801 = df287.copy()
df801['车厢'] = df801['车厢'].astype(str).str.zfill(2)
df801['Source'] = df801['车组']+ '_' + df801['车厢']
df801['Platform ID'] = df801['Current_Station'].apply(lambda idxx : map_id(idxx))
df801["Current_Station"]= df801["Current_Station"].apply(lambda name : map_stname(name))
df801['Type'] = df801['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df801['Type'] = 'T' + df801['Type']
df801['sort1']= df801['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df801['sort2']= df801['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df801['sort1'] = df801['sort1'].astype("int")
df801['sort2'] = df801['sort2'].astype("int")
df801 = df801.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df801 = df801.fillna('               // ')
df801 = df801.dropna(axis = 0 ,how = 'any')
df801 = df801.reindex(columns=['Source','预警时间','Current_Station','Platform ID','Type'])


# VCB Excel File (Group Count)   -->  df802 , df803

df802 = df801.copy()
df802 = pd.DataFrame(df802.groupby(['Source']).size(),columns=['VCB Count']).reset_index()
df802 = df802.reindex(columns=['Source','VCB Count'])
df802 = df802.sort_values(by='VCB Count',ascending = False)
df802['Type'] = df802['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df802['Type'] = 'T' + df802['Type']
df802['sort1']= df802['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df802['sort2']= df802['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df802['sort1'] = df802['sort1'].astype("int")
df802['sort2'] = df802['sort2'].astype("int")
df802 = df802.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df803 = df802.nlargest(n = 10 , columns =['VCB Count'])


# Selector of VCB Alarm (For DropDownList [Trainset])  -->  df804
df804 = df801.copy()
df804['sort1']= df804['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df804['sort2']= df804['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df804['sort1'] = df804['sort1'].astype("int")
df804['sort2'] = df804['sort2'].astype("int")
df804 = df804.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)


#Top 1 No. of VCB Alarm Trend--> df291
try:
    top1 = df803.iloc[0]['Source']
    df291 = df801.copy()
    df291 = df291.loc[(df291['Source'] == top1)]
    df291['预警时间'] = df291['预警时间'].str.slice(0,10)
    df291= pd.DataFrame(df291.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df291 = df291.sort_values(by=['预警时间'])
    ax = df291.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df291.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top1 +' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top1.png'.format(user,top1))
    plt.close()
    
except:
    print('No Top1 VCB Trend')
    plt.close()



#Top 2 No. of VCB Alarm Trend--> df292
try:
    top2 = df803.iloc[1]['Source']
    df292 = df801.copy()
    df292 = df292.loc[(df292['Source'] == top2)]
    df292['预警时间'] = df292['预警时间'].str.slice(0,10)
    df292= pd.DataFrame(df292.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df292 = df292.sort_values(by=['预警时间'])
    ax = df292.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df292.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top2 +' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top2.png'.format(user,top2))
    plt.close()
    
except:
    print('No Top2 VCB Trend')
    plt.close()



#Top 3 No. of VCB Alarm Trend--> df293
try:
    top3 = df803.iloc[2]['Source']
    df293 = df801.copy()
    df293 = df293.loc[(df293['Source'] == top3)]
    df293['预警时间'] = df293['预警时间'].str.slice(0,10)
    df293= pd.DataFrame(df293.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df293 = df293.sort_values(by=['预警时间'])
    ax = df293.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df293.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top3 +' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top3.png'.format(user,top3))
    plt.close()
    
except:
    print('No Top3 VCB Trend')
    plt.close()



#Top 4 No. of VCB Alarm Trend--> df294
try:
    top4 = df803.iloc[3]['Source']
    df294 = df801.copy()
    df294 = df294.loc[(df294['Source'] == top4)]
    df294['预警时间'] = df294['预警时间'].str.slice(0,10)
    df294= pd.DataFrame(df294.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df294 = df294.sort_values(by=['预警时间'])
    ax = df294.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df294.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top4 +' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top4.png'.format(user,top4))
    plt.close()
    
except:
    print('No Top4 VCB Trend')
    plt.close()



#Top 5 No. of VCB Alarm Trend--> df295
try:
    top5= df803.iloc[4]['Source']
    df295 = df801.copy()
    df295 = df295.loc[(df295['Source'] == top5)]
    df295['预警时间'] = df295['预警时间'].str.slice(0,10)
    df295= pd.DataFrame(df295.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df295 = df295.sort_values(by=['预警时间'])
    ax = df295.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df295.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top5+' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top5.png'.format(user,top5))
    plt.close()
    
except:
    print('No Top5 VCB Trend')
    plt.close()



#Top 6 No. of VCB Alarm Trend--> df296
try:
    top6= df803.iloc[5]['Source']
    df296 = df801.copy()
    df296 = df296.loc[(df296['Source'] == top6)]
    df296['预警时间'] = df296['预警时间'].str.slice(0,10)
    df296= pd.DataFrame(df296.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df296 = df296.sort_values(by=['预警时间'])
    ax = df296.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df296.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top6+' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top6.png'.format(user,top6))
    plt.close()
    
except:
    print('No Top6 VCB Trend')
    plt.close()



#Top 7 No. of VCB Alarm Trend--> df297
try:
    top7= df803.iloc[6]['Source']
    df297 = df801.copy()
    df297 = df297.loc[(df297['Source'] == top7)]
    df297['预警时间'] = df297['预警时间'].str.slice(0,10)
    df297= pd.DataFrame(df297.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df297 = df297.sort_values(by=['预警时间'])
    ax = df297.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df297.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top7+' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top7.png'.format(user,top7))
    plt.close()
    
except:
    print('No Top7 VCB Trend')
    plt.close()



#Top 8 No. of VCB Alarm Trend--> df298
try:
    top8= df803.iloc[7]['Source']
    df298 = df801.copy()
    df298 = df298.loc[(df298['Source'] == top8)]
    df298['预警时间'] = df298['预警时间'].str.slice(0,10)
    df298= pd.DataFrame(df298.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df298 = df298.sort_values(by=['预警时间'])
    ax = df298.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df298.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top8+' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top8.png'.format(user,top8))
    plt.close()
    
except:
    print('No Top8 VCB Trend')
    plt.close()



#Top 9 No. of VCB Alarm Trend--> df299
try:
    top9= df803.iloc[8]['Source']
    df299 = df801.copy()
    df299 = df299.loc[(df299['Source'] == top9)]
    df299['预警时间'] = df299['预警时间'].str.slice(0,10)
    df299= pd.DataFrame(df299.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df299 = df299.sort_values(by=['预警时间'])
    ax = df299.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df299.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top9+' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top9.png'.format(user,top9))
    plt.close()
    
except:
    print('No Top9 VCB Trend')
    plt.close()



#Top 10 No. of VCB Alarm Trend--> df300
try:
    top10= df803.iloc[9]['Source']
    df300 = df801.copy()
    df300 = df300.loc[(df300['Source'] == top10)]
    df300['预警时间'] = df300['预警时间'].str.slice(0,10)
    df300= pd.DataFrame(df300.groupby(['Source' ,'预警时间']).size(),columns=['VCB Count']).reset_index()
    df300 = df300.sort_values(by=['预警时间'])
    ax = df300.plot.scatter(x= '预警时间', y= 'VCB Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df300.plot.line(x= '预警时间', y='VCB Count', ax=ax, style='b',rot=25)
    plt.title(top10+' '+ 'VCB Trend')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.savefig(r'C:\Users\{0}\Downloads\location\VCB\Top_Ten\Top_Ten_Trend\{1}_Top10.png'.format(user,top10))
    plt.close()
    
except:
    print('No Top10 VCB Trend')
    plt.close()


# Top Ten VCB Trend Graphs (Group by Source & Occurring Time)  -->  df805
try:
    df805 = pd.concat([df291,df292,df293,df294,df295,df296,df297,df298,df299,df300], axis = 0)

except:
    pass


# Change datetime to date (Formatting)
StartDate = StartDate.date()
EndDate = EndDate.date()

# Create a dashborad for VCB Alarm
try:
 
# fig --> All Trainset VCB Group Count Graph


    fig = px.bar(df800,x='车组',
             y='VCB Count',
             title = f'All Trainset VCB Group Count',
             hover_name='车组')

# fig1 --> All Top Ten VCB Trend Graph

    fig1 = px.bar(df803,x='Source',
              y='VCB Count',
              title = f'Top Ten VCB Trend',
              hover_name='Source')


    layout = html.Div([
        html.Div([html.Header("VCB Alarm"),
        html.Div([dcc.Dropdown(id="mydropdown",
                 options = df804['Type'].unique(),
                 value = df804.iloc[0]['Type']),
        dcc.Graph(id = 'all_graphs1')],className ='six columns'),
        html.Div([
            dcc.Graph(id = 'one_graph',figure = fig)],className= 'five columns'),],className = 'row'),
        html.Div([html.H2("Data", style={"textAlign":"center"}),
        html.Hr(),
        html.Div(id='table6',children = 'Excel'),],className='row'),
        html.H2("Trend", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([dcc.Dropdown(id="mydropdown2",
              options = df803['Source'].unique(),
              value = df803.iloc[0]['Source'],
            ),
        dcc.Graph(id = 'trend_graphs1')],className ='six columns'),
        html.Div([
            dcc.Graph(id = 'top_ten_trend',figure = fig1)],className ='five columns'),
        
        ])
    
   

    @app.callback(
        Output('all_graphs1','figure'),
        Output('table6', 'children'),
        Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df801.loc[df801['Type']==changes]
        filtered_data2 = df802.loc[df802['Type']==changes]
        a = filtered_data2.nlargest(n=1,columns=['VCB Count'])
        a = a.iloc[0]['Source']
        fig_bar = px.bar(filtered_data2,
                x='Source',
                y='VCB Count',
                title =f'The Highest VCB Alarm Train : {a}',
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
     Output('trend_graphs1','figure'),
     Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df805.loc[df805['Source']==changes]

        fig_top_trends = px.line(fil_data.loc[fil_data['Source']==changes],
                x='预警时间',
                y='VCB Count',
                title =f'VCB Trend',
                hover_name = 'Source',
                markers = True)
    
        return fig_top_trends




except:
    print('No VCB Dashboard')
