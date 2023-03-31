
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
from load_data import get_dataframe , map_id, map_stname, user
from dash import Dash, dcc, html, Input, Output, dash_table

df6 = get_dataframe()

# Main Pressure Fall Alarm Excel Files  -->  df181
df181 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df181['Pressure Fall'] = df181['预警描述'].str.extract('(?:.*Main Pressure fall)(-[0.0-9.0]+)')
df181['Pressure Fall'] = df181['Pressure Fall'].astype("float")

df181 = df181.reindex(columns=['车组','车厢','预警时间','Pressure Fall','预警描述'])
df181 = df181.dropna(axis = 0 ,how = 'any')
df181 = df181.reset_index(drop=True)


# Main Pressure Fall Standard  -->  df182
df182 = df181.copy()
df182['Hi'] = df182['预警描述'].str.extract('(?:.*<)(-[0.0-9.0]+)(?:)')
df182 = df182.dropna(axis=0,how='any')
df182.loc[(df182['预警描述'].str.contains('Main Pressure fall') == True),'Main Pressure Fall Standard'] = '< ' + df182['Hi']
df182 = df182.dropna(axis = 0, how = 'any')
df182 = pd.DataFrame(df182['Main Pressure Fall Standard'])[:1]
df182 = df182.reset_index(drop = True)


# Pressure Fall Excel Files in Dashboard
df184 = df181.copy()
df184 = pd.DataFrame(df184.groupby(['Pressure Fall']).size(),columns=['Pressure Fall Count']).reset_index()
df184['Pressure Fall'] = df184['Pressure Fall'].astype('str')
df183 = pd.DataFrame(pd.concat([df181,df182],axis=1))
df183['车厢'] = df183['车厢'].astype(str).str.zfill(2)
df183['Source'] = df183['车组']+ '_' + df183['车厢']
df183['sort1']= df183['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df183['sort2']= df183['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
df183['sort1'] = df183['sort1'].astype("int")
df183['sort2'] = df183['sort2'].astype("int")
df183 = df183.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = True)
df183 = df183.fillna('               // ')
df183 = df183.dropna(axis = 0 ,how = 'any')
df183 = df183.reindex(columns=['Source','预警时间','Pressure Fall','Main Pressure Fall Standard'])



# Main Pressure Fall Excel File (Group Count)   -->  df199
try:
    df199 = df183.copy()
    df199 = pd.DataFrame(df199.groupby(['Source','Pressure Fall']).size(),columns=['Pressure Fall Count']).reset_index()
    df199 = df199.reindex(columns=['Source','Pressure Fall','Pressure Fall Count'])
    df199 = df199.sort_values(by='Pressure Fall Count',ascending = False)
    df200 = df199.nlargest(n = 10 , columns =['Pressure Fall Count'])

except:

    pass


# For sorting the dropdownlist (-0.000--> -0.009)
df410 = pd.DataFrame(df183['Pressure Fall'])
df410 = df410.sort_values(by=['Pressure Fall'],ascending = False)


#Top 1 No. of Pressure Fall Alarm Trend--> df202
try:
    top1 = df200.iloc[0]['Source']
    t1_speed= df200.iloc[0]['Pressure Fall']
    df202 = df183.copy()
    df202 = df202.loc[(df202['Source'] == top1) & (df202['Pressure Fall'] == t1_speed)]
    df202['预警时间'] = df202['预警时间'].str.slice(0,10)
    df202= pd.DataFrame(df202.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df202 = df202.sort_values(by=['预警时间'])
    ax = df202.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df202.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top1 +' '+ 'Main Pressure Fall Trend ({})'.format(t1_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top1.png'.format(user,top1))
    plt.close()
    
except:
    print('No Top1 Main Pressure Fall Trend')
    plt.close()



#Top 2 No. of Pressure Fall Alarm Trend--> df204
try:
    top2 = df200.iloc[1]['Source']
    t2_speed= df200.iloc[1]['Pressure Fall']
    df204 = df183.copy()
    df204 = df204.loc[(df204['Source'] == top2) & (df204['Pressure Fall'] == t2_speed)]
    df204['预警时间'] = df204['预警时间'].str.slice(0,10)
    df204= pd.DataFrame(df204.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df204 = df204.sort_values(by=['预警时间'])
    ax = df204.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df204.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top2 +' '+ 'Main Pressure Fall Trend ({})'.format(t2_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top2.png'.format(user,top2))
    plt.close()
    
except:
    print('No Top2 Main Pressure Fall Trend')
    plt.close()


#Top 3 No. of Pressure Fall Alarm Trend--> df205
try:
    top3 = df200.iloc[2]['Source']
    t3_speed= df200.iloc[2]['Pressure Fall']
    df205 = df183.copy()
    df205 = df205.loc[(df205['Source'] == top3) & (df205['Pressure Fall'] == t3_speed)]
    df205['预警时间'] = df205['预警时间'].str.slice(0,10)
    df205= pd.DataFrame(df205.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df205 = df205.sort_values(by=['预警时间'])
    ax = df205.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df205.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top3 +' '+ 'Main Pressure Fall Trend ({})'.format(t3_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top3.png'.format(user,top3))
    plt.close()
    
except:
    print('No Top3 Main Pressure Fall Trend')
    plt.close()


#Top 4 No. of Pressure Fall Alarm Trend--> df206
try:
    top4 = df200.iloc[3]['Source']
    t4_speed= df200.iloc[3]['Pressure Fall']
    df206 = df183.copy()
    df206 = df206.loc[(df206['Source'] == top4) & (df206['Pressure Fall'] == t4_speed)]
    df206['预警时间'] = df206['预警时间'].str.slice(0,10)
    df206= pd.DataFrame(df206.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df206 = df206.sort_values(by=['预警时间'])
    ax = df206.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df206.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top4 +' '+ 'Main Pressure Fall Trend ({})'.format(t4_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top4.png'.format(user,top4))
    plt.close()
    
except:
    print('No Top4 Main Pressure Fall Trend')
    plt.close()


#Top 5 No. of Pressure Fall Alarm Trend--> df207
try:
    top5 = df200.iloc[4]['Source']
    t5_speed= df200.iloc[4]['Pressure Fall']
    df207 = df183.copy()
    df207 = df207.loc[(df207['Source'] == top5) & (df207['Pressure Fall'] == t5_speed)]
    df207['预警时间'] = df207['预警时间'].str.slice(0,10)
    df207= pd.DataFrame(df207.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df207 = df207.sort_values(by=['预警时间'])
    ax = df207.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df207.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top5 +' '+ 'Main Pressure Fall Trend ({})'.format(t5_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top5.png'.format(user,top5))
    plt.close()
    
except:
    print('No Top5 Main Pressure Fall Trend')
    plt.close()


#Top 6 No. of Pressure Fall Alarm Trend--> df208
try:
    top6 = df200.iloc[5]['Source']
    t6_speed= df200.iloc[5]['Pressure Fall']
    df208 = df183.copy()
    df208 = df208.loc[(df208['Source'] == top6) & (df208['Pressure Fall'] == t6_speed)]
    df208['预警时间'] = df208['预警时间'].str.slice(0,10)
    df208= pd.DataFrame(df208.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df208 = df208.sort_values(by=['预警时间'])
    ax = df208.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df208.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top6 +' '+ 'Main Pressure Fall Trend ({})'.format(t6_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top6.png'.format(user,top6))
    plt.close()
    
except:
    print('No Top6 Main Pressure Fall Trend')
    plt.close()


#Top 7 No. of Pressure Fall Alarm Trend--> df209
try:
    top7 = df200.iloc[6]['Source']
    t7_speed= df200.iloc[6]['Pressure Fall']
    df209 = df183.copy()
    df209 = df209.loc[(df209['Source'] == top7) & (df209['Pressure Fall'] == t7_speed)]
    df209['预警时间'] = df209['预警时间'].str.slice(0,10)
    df209= pd.DataFrame(df209.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df209 = df209.sort_values(by=['预警时间'])
    ax = df209.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df209.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top7 +' '+ 'Main Pressure Fall Trend ({})'.format(t7_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top7.png'.format(user,top7))
    plt.close()
    
except:
    print('No Top7 Main Pressure Fall Trend')
    plt.close()


#Top 8 No. of Pressure Fall Alarm Trend--> df210
try:
    top8 = df200.iloc[7]['Source']
    t8_speed= df200.iloc[7]['Pressure Fall']
    df210 = df183.copy()
    df210 = df210.loc[(df210['Source'] == top8) & (df210['Pressure Fall'] == t8_speed)]
    df210['预警时间'] = df210['预警时间'].str.slice(0,10)
    df210= pd.DataFrame(df210.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df210 = df210.sort_values(by=['预警时间'])
    ax = df210.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df210.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top8 +' '+ 'Main Pressure Fall Trend ({})'.format(t8_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top8.png'.format(user,top8))
    plt.close()
    
except:
    print('No Top8 Main Pressure Fall Trend')
    plt.close()


#Top 9 No. of Pressure Fall Alarm Trend--> df211
try:
    top9 = df200.iloc[8]['Source']
    t9_speed= df200.iloc[8]['Pressure Fall']
    df211 = df183.copy()
    df211 = df211.loc[(df211['Source'] == top9) & (df211['Pressure Fall'] == t9_speed)]
    df211['预警时间'] = df211['预警时间'].str.slice(0,10)
    df211= pd.DataFrame(df211.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df211 = df211.sort_values(by=['预警时间'])
    ax = df211.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df211.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top9 +' '+ 'Main Pressure Fall Trend ({})'.format(t9_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top9.png'.format(user,top9))
    plt.close()
    
except:
    print('No Top9 Main Pressure Fall Trend')
    plt.close()


#Top 10 No. of Pressure Fall Alarm Trend--> df212
try:
    top10 = df200.iloc[9]['Source']
    t10_speed= df200.iloc[9]['Pressure Fall']
    df212 = df183.copy()
    df212 = df212.loc[(df212['Source'] == top10) & (df212['Pressure Fall'] == t10_speed)]
    df212['预警时间'] = df212['预警时间'].str.slice(0,10)
    df212= pd.DataFrame(df212.groupby(['Source' ,'预警时间']).size(),columns=['Pressure Fall Count']).reset_index()
    df212 = df212.sort_values(by=['预警时间'])
    ax = df212.plot.scatter(x= '预警时间', y= 'Pressure Fall Count', style='b',figsize = (12,12))
    ax.yaxis.get_major_locator().set_params(integer=True)
    df212.plot.line(x= '预警时间', y='Pressure Fall Count', ax=ax, style='b',rot=25)
    plt.title(top10 +' '+ 'Main Pressure Fall Trend ({})'.format(t10_speed))
    plt.ylabel('Count')
    plt.xlabel('Date')
    #plt.savefig(r'C:\Users\{0}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Pressure_Fall_Trend\{1}_Top10.png'.format(user,top10))
    plt.close()
    
except:
    print('No Top10 Main Pressure Fall Trend')
    plt.close()


# Top Ten Pressure Fall Trend Graphs (Group by Source & Occurring Time)  -->  df411
try:
    df411 = pd.DataFrame(pd.concat([df202,df204,df205,df206,df207,df208,df209,df210,df211,df212],axis = 0))
    df411 = df411.reset_index()

except:
    pass

# Create a a dashboard for Pressure Fall Alarm

# fig --> Top Ten Pressure Fall Distribution Graph
try:
    fig = px.bar(df200,x='Source',
                y='Pressure Fall Count',
                title = f'Top Ten Pressure Fall Graph',
                color = 'Pressure Fall',
                hover_name = 'Source')

# fig1 --> Pressure Fall Distribution Graph

    fig1 = px.bar(df184,
                  x='Pressure Fall',
                  y='Pressure Fall Count',
                  title =f'Pressure Fall Distribution',
                  hover_name = 'Pressure Fall')
             


    layout = html.Div([
        html.Div([html.Header("Pressure Fall"),
        html.Div([
             dcc.Dropdown(id="mydropdown",
                         options = sorted(df410['Pressure Fall'].unique(),reverse = True),
                         value = df410.iloc[0]['Pressure Fall']),
            dcc.Graph(id = 'fall_distri')],className= 'six columns'),
        html.Div([dcc.Graph(id ='all_fall_distri',figure = fig1)],className ='five columns'),],className='row'),     
        html.Div([html.H2("Data", style={"textAlign":"center"}),
        html.Hr(),
        html.Div(id='table5',children = 'Excel')],className='row'),
        #dcc.Graph(id = 'my_mini_plot')
        html.H2("Trend", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([
            dcc.Dropdown(id="mydropdown2",
                        options = df411['Source'].unique(),
                        value = df411.iloc[0]['Source']),
            dcc.Graph(id = 'top_ten_trends3')],className ='five columns'),
        html.Div([dcc.Graph(id='top_ten_fall',figure = fig)],className = 'five columns'),
        ])




    @app.callback(
        #Output('my_mini_plot','figure'),
        Output('fall_distri', 'figure'),
        Output('table5','children'),
        Input('mydropdown','value')
    )


    def sync_input(changes):

        filtered_data = df199.loc[df199['Pressure Fall']==changes]
        filtered_data2 = df183.loc[df183['Pressure Fall']==changes]
    
        fig_fall_dis = px.bar(filtered_data,
                    x='Source',
                    y='Pressure Fall Count',
                    title =f'Pressure Fall Distribution (Filter)',
                    hover_name = 'Source',
                    hover_data =['Pressure Fall Count'])
    

    
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
    

    
    
    
        return fig_fall_dis , tb


    @app.callback(
        Output('top_ten_trends3','figure'),
        Input('mydropdown2','value')

    )

    def trend_input(changes):
        fil_data = df411.loc[df411['Source']==changes]
    
    
        fig_top_trend = px.line(fil_data,
                                x='预警时间',
                                y='Pressure Fall Count',
                                title = f'Top Ten Trend Graphs',
                                hover_name = 'Source',
                                markers = True
                                )
        return fig_top_trend

except:
    print ('No Pressure Fall Dashboard')
