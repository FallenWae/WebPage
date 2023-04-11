
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

# Main Pressure Rise Alarm Excel Files  -->  df176

df176 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df176['Pressure Rise'] = df176['预警描述'].str.extract('(?:.*Main Pressure rise)([0.0-9.0]+)')
df176['Pressure Rise'] = df176['Pressure Rise'].astype("float")

df176 = df176.reindex(columns=['车组','车厢','预警时间','Pressure Rise','预警描述'])
df176 = df176.dropna(axis = 0 ,how = 'any')
df176 = df176.reset_index(drop=True)


# Main Pressure Rise Standard  -->  df177
df177 = df176.copy()
df177['Hi'] = df177['预警描述'].str.extract('(?:.*<)([0.0-9.0]+)(?:)')
df177 = df177.drop(df177[df177['Hi'] == '0'].index, axis = 'rows')
df177 = df177.dropna(axis=0,how='any')
df177.loc[(df177['预警描述'].str.contains('Main Pressure rise') == True),'Main Pressure Rise Standard'] = '< ' + df177['Hi']
df177 = df177.dropna(axis = 0, how = 'any')
df177 = pd.DataFrame(df177['Main Pressure Rise Standard'])[:1]
df177 = df177.reset_index(drop = True)


# Pressure Rise Excel Files in Dashboard
df179 = df176.copy()
df179 = pd.DataFrame(df179.groupby(['Pressure Rise']).size(),columns=['Pressure Rise Count']).reset_index()
df178 = pd.DataFrame(pd.concat([df176,df177],axis=1))
df178['车厢'] = df178['车厢'].astype(str).str.zfill(2)
df178['Source'] = df178['车组']+ '_' + df178['车厢']
df178['sort1']= df178['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df178['sort2']= df178['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df178['sort1'] = df178['sort1'].astype("int")
df178['sort2'] = df178['sort2'].astype("int")
df178 = df178.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df178 = df178.fillna('               // ')
df178 = df178.dropna(axis = 0 ,how = 'any')
df178 = df178.reindex(columns=['Source','预警时间','Pressure Rise','Main Pressure Rise Standard'])


# Main Pressure Rise Excel File (Group Count)   -->  df187
try:
    df187 = df178.copy()
    df187 = pd.DataFrame(df187.groupby(['Source','Pressure Rise']).size(),columns=['Pressure Rise Count']).reset_index()
    df187 = df187.reindex(columns=['Source','Pressure Rise','Pressure Rise Count'])
    df187 = df187.sort_values(by='Pressure Rise Count',ascending = False)
    df188 = df187.nlargest(n = 10 , columns =['Pressure Rise Count'])
    df187['sort1']= df187['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df187['sort2']= df187['Source'].str.extract('(?:.*_)([0-9]+)')
    df187['sort1'] = df187['sort1'].astype("int")
    df187['sort2'] = df187['sort2'].astype("int")
    df187 = df187.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)

except:

    pass


# For sorting the dropdownlist (0.000--> 0.009)
df408 = pd.DataFrame(df178['Pressure Rise'])
df408 = df408.sort_values(by=['Pressure Rise'])


#Top 1 No. of Pressure Rise Alarm Trend--> df189
try:
    top1 = df188.iloc[0]['Source']
    t1_speed= df188.iloc[0]['Pressure Rise']
    df189 = df178.copy()
    df189 = df189.loc[(df189['Source'] == top1) & (df189['Pressure Rise'] == t1_speed)]
    df189['预警时间'] = df189['预警时间'].str.slice(0,10)
    df189= pd.DataFrame(df189.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df189 = df189.sort_values(by=['预警时间'])
    ax = df189.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df189.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top1 +' '+ 'Main Pressure Rise Trend ({})'.format(t1_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top1.png'.format(user,top1))
    plt.close()
    
except:
    print('No Top1 Main Pressure Rise Trend')
    plt.close()


#Top 2 No. of Pressure Rise Alarm Trend --> df190
try:
    top2 = df188.iloc[1]['Source']
    t2_speed= df188.iloc[1]['Pressure Rise']
    df190 = df178.copy()
    df190 = df190.loc[(df190['Source'] == top2) & (df190['Pressure Rise'] == t2_speed)]
    df190['预警时间'] = df190['预警时间'].str.slice(0,10)
    df190= pd.DataFrame(df190.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df190 = df190.sort_values(by=['预警时间'])
    ax = df190.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df190.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top2 +' '+ 'Main Pressure Rise Trend ({})'.format(t2_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top2.png'.format(user,top2))
    plt.close()
    
except:
    print('No Top2 Main Pressure Rise Trend')
    plt.close()


#Top 3 No. of Pressure Rise Alarm Trend --> df191
try:
    top3 = df188.iloc[2]['Source']
    t3_speed= df188.iloc[2]['Pressure Rise']
    df191 = df178.copy()
    df191 = df191.loc[(df191['Source'] == top3) & (df191['Pressure Rise'] == t3_speed)]
    df191['预警时间'] = df191['预警时间'].str.slice(0,10)
    df191= pd.DataFrame(df191.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df191 = df191.sort_values(by=['预警时间'])
    ax = df191.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df191.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top3 +' '+ 'Main Pressure Rise Trend ({})'.format(t3_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top3.png'.format(user,top3))
    plt.close()
    
except:
    print('No Top3 Main Pressure Rise Trend')
    plt.close()


#Top 4 No. of Pressure Rise Alarm Trend --> df192
try:
    top4 = df188.iloc[3]['Source']
    t4_speed= df188.iloc[3]['Pressure Rise']
    df192 = df178.copy()
    df192 = df192.loc[(df192['Source'] == top4) & (df192['Pressure Rise'] == t4_speed)]
    df192['预警时间'] = df192['预警时间'].str.slice(0,10)
    df192= pd.DataFrame(df192.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df192 = df192.sort_values(by=['预警时间'])
    ax = df192.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df192.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top4 +' '+ 'Main Pressure Rise Trend ({})'.format(t4_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top4.png'.format(user,top4))
    plt.close()
    
except:
    print('No Top4 Main Pressure Rise Trend')
    plt.close()


#Top 5 No. of Pressure Rise Alarm Trend --> df193
try:
    top5 = df188.iloc[4]['Source']
    t5_speed= df188.iloc[4]['Pressure Rise']
    df193 = df178.copy()
    df193 = df193.loc[(df193['Source'] == top5) & (df193['Pressure Rise'] == t5_speed)]
    df193['预警时间'] = df193['预警时间'].str.slice(0,10)
    df193= pd.DataFrame(df193.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df193 = df193.sort_values(by=['预警时间'])
    ax = df193.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df193.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top5 +' '+ 'Main Pressure Rise Trend ({})'.format(t5_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top5.png'.format(user,top5))
    plt.close()
    
except:
    print('No Top5 Main Pressure Rise Trend')
    plt.close()


#Top 6 No. of Pressure Rise Alarm Trend --> df194
try:
    top6 = df188.iloc[5]['Source']
    t6_speed= df188.iloc[5]['Pressure Rise']
    df194 = df178.copy()
    df194 = df194.loc[(df194['Source'] == top6) & (df194['Pressure Rise'] == t6_speed)]
    df194['预警时间'] = df194['预警时间'].str.slice(0,10)
    df194= pd.DataFrame(df194.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df194 = df194.sort_values(by=['预警时间'])
    ax = df194.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df194.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top6 +' '+ 'Main Pressure Rise Trend ({})'.format(t6_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top6.png'.format(user,top6))
    plt.close()
    
except:
    print('No Top6 Main Pressure Rise Trend')
    plt.close()


#Top 7 No. of Pressure Rise Alarm Trend --> df195
try:
    top7 = df188.iloc[6]['Source']
    t7_speed= df188.iloc[6]['Pressure Rise']
    df195 = df178.copy()
    df195 = df195.loc[(df195['Source'] == top7) & (df195['Pressure Rise'] == t7_speed)]
    df195['预警时间'] = df195['预警时间'].str.slice(0,10)
    df195= pd.DataFrame(df195.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df195 = df195.sort_values(by=['预警时间'])
    ax = df195.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df195.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top7 +' '+ 'Main Pressure Rise Trend ({})'.format(t7_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top7.png'.format(user,top7))
    plt.close()
    
except:
    print('No Top7 Main Pressure Rise Trend')
    plt.close()


#Top 8 No. of Pressure Rise Alarm Trend --> df196
try:
    top8 = df188.iloc[7]['Source']
    t8_speed= df188.iloc[7]['Pressure Rise']
    df196 = df178.copy()
    df196 = df196.loc[(df196['Source'] == top8) & (df196['Pressure Rise'] == t8_speed)]
    df196['预警时间'] = df196['预警时间'].str.slice(0,10)
    df196= pd.DataFrame(df196.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df196 = df196.sort_values(by=['预警时间'])
    ax = df196.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df196.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top8 +' '+ 'Main Pressure Rise Trend ({})'.format(t8_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top8.png'.format(user,top8))
    plt.close()
    
except:
    print('No Top8 Main Pressure Rise Trend')
    plt.close()


#Top 9 No. of Pressure Rise Alarm Trend --> df197
try:
    top9 = df188.iloc[8]['Source']
    t9_speed= df188.iloc[8]['Pressure Rise']
    df197 = df178.copy()
    df197 = df197.loc[(df197['Source'] == top9) & (df197['Pressure Rise'] == t9_speed)]
    df197['预警时间'] = df197['预警时间'].str.slice(0,10)
    df197= pd.DataFrame(df197.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df197 = df197.sort_values(by=['预警时间'])
    ax = df197.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df197.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top9 +' '+ 'Main Pressure Rise Trend ({})'.format(t9_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top9.png'.format(user,top9))
    plt.close()
    
except:
    print('No Top9 Main Pressure Rise Trend')
    plt.close()


#Top 10 No. of Pressure Rise Alarm Trend --> df198
try:
    top10 = df188.iloc[9]['Source']
    t10_speed= df188.iloc[9]['Pressure Rise']
    df198 = df178.copy()
    df198 = df198.loc[(df198['Source'] == top10) & (df198['Pressure Rise'] == t10_speed)]
    df198['预警时间'] = df198['预警时间'].str.slice(0,10)
    df198= pd.DataFrame(df198.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Rise Count']).reset_index()
    df198 = df198.sort_values(by=['预警时间'])
    ax = df198.plot.scatter(x= '预警时间', y= 'Pressure Rise Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df198.plot.line(x= '预警时间', y='Pressure Rise Count', ax=ax, style='b',rot=25)
    plt.title(top10 +' '+ 'Main Pressure Rise Trend ({})'.format(t10_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Pressure_Rise_Trend\{1}_Top10.png'.format(user,top10))
    plt.close()
    
except:
    print('No Top10 Main Pressure Rise Trend')
    plt.close()



# Top Ten Pressure Rise Trend Graphs (Group by Source & Occurring Time)  -->  df409
try:
    df409 = pd.DataFrame(pd.concat([df189,df190,df191,df192,df193,df194,df195,df196,df197,df198],axis = 0))
    df409 = df409.reset_index()

except:
    pass


# Change datetime to date (Formatting)
StartDate = StartDate.date()
EndDate = EndDate.date()

# Create a a dashboard for Pressure Rise Alarm

# fig --> Top Ten Opening Speed Distribution Graph
try:
    fig = px.bar(df188,x='Source',
                y='Pressure Rise Count',
                title = f'Top Ten Pressure Rise Graph',
                color = 'Pressure Rise',
                hover_name = 'Source')

# fig1 --> Opening Speed Distribution Graph


    fig1 = px.bar(df179,
                  x='Pressure Rise',
                  y='Pressure Rise Count',
                  title =f'Pressure Rise Distribution',
                hover_name = 'Pressure Rise')
    fig1.update_xaxes(dtick = 0.001)
             


    layout = html.Div([
     html.Div([html.Header(f"Pressure Rise ({StartDate} to {EndDate})"),
     html.Div([
             dcc.Dropdown(id="mydropdown",
                         options = sorted(df408['Pressure Rise'].unique()),
                         value = df408.iloc[0]['Pressure Rise']),
            dcc.Graph(id = 'rise_distri')],className= 'six columns'),
        html.Div([dcc.Graph(id ='all_rise_distri',figure = fig1)],className ='five columns'),],className='row'),     
        html.Div([html.H2("Data", style={"textAlign":"center"}),
        html.Hr(),
        html.Div(id='table4',children = 'Excel')],className='row'),
        html.H2("Trend", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([
             dcc.Dropdown(id="mydropdown2",
                          options = df409['Source'].unique(),
                          value = df409.iloc[0]['Source']),
            dcc.Graph(id = 'top_ten_trends2')],className ='five columns'),
        html.Div([dcc.Graph(id='top_ten_rise',figure = fig)],className = 'five columns'),
        ])




    @app.callback(
     Output('rise_distri', 'figure'),
     Output('table4','children'),
     Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df187.loc[df187['Pressure Rise']==changes]
        filtered_data2 = df178.loc[df178['Pressure Rise']==changes]
        
        a = filtered_data.nlargest(n=1,columns=['Pressure Rise Count'])
        a = a.iloc[0]['Source']
    
        fig_rise_dis = px.bar(filtered_data,
                  x='Source',
                  y='Pressure Rise Count',
                  title =f'Pressure Rise Distribution (Filter)\nThe Highest Pressure Rise Train : {a}',
                  hover_name = 'Source',
                  hover_data =['Pressure Rise Count'])
    
    
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
    

    
    
    
        return fig_rise_dis , tb


    @app.callback(
        Output('top_ten_trends2','figure'),
        Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df409.loc[df409['Source']==changes]
    
    
        fig_top_trend = px.line(fil_data,
                                x='预警时间',
                                y='Pressure Rise Count',
                                title = f'Top Ten Trend Graphs',
                                hover_name = 'Source',
                                markers = True
                                )
        return fig_top_trend

except:
    print('Not Pressure Time Dashboard')



