
#!/usr/bin/env python
# coding: utf-8

# In[1]:
from app import app
from app import server
from dash import Dash, html, dcc, Input, Output, dash_table, State
from load_data import  StartDate, EndDate
import pandas as pd
import dash_bootstrap_components as dbc 

from pages import obs_alarm, op_alarm, cl_alarm, prise_alarm, pfall_alarm

alarms_list = ['obs_alarm', 'op_alarm', 'cl_alarm', 'prise_alarm', 'pfall_alarm']

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",
}


SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


# Change datetime to date (Formatting)
StartDate = StartDate.date()
EndDate = EndDate.date()


navbar = dbc.NavbarSimple(
    children=[
        
           dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Alarms", header=True),
                dbc.DropdownMenuItem("Obstacle Detected Alarm", href="/pages/obs_alarm"),
                dbc.DropdownMenuItem("Opening Time Alarm", href="/pages/op_alarm"),
                dbc.DropdownMenuItem("Closing Time Alarm", href="/pages/cl_alarm"),
                dbc.DropdownMenuItem("Pressure Rise Alarm", href="/pages/prise_alarm"),
                dbc.DropdownMenuItem("Pressure Fall Alarm", href="/pages/pfall_alarm"),
            ],
            nav=True,
            in_navbar=True,
            label="Alarms",
            size = 'lg',
        ),
        dbc.Button("Sidebar" , color="secondary", className="mr-1", id="btn_sidebar"),
     
    ],
    brand = 'PHM Alarms',
    brand_href ='/pages/obs_alarm',
    color="dark",
    dark=True,
    fluid=True,
    links_left=True,
    sticky='Top'
)

sidebar = html.Div(
    [

    html.H2('Sidebar', className='display-4'),
    html.Hr(),
    html.P('PHM Alarms', className = 'lead'),
    
    dbc.Nav(
        [  
            dbc.NavLink("Obstacle Detected", href="/pages/obs_alarm", id = 'obs_alarm_link'),
            dbc.NavLink("Opening Time", href="/pages/op_alarm", id = 'op_alarm_link'),
            dbc.NavLink("Closing Time", href="/pages/cl_alarm", id = 'cl_alarm_link'),
            dbc.NavLink("Pressure Rise", href="/pages/prise_alarm", id = 'prise_alarm_link'),
            dbc.NavLink("Pressure Fall", href="/pages/pfall_alarm", id = 'pfall_alarm_link'),
        ],
        vertical=True,
        pills=True,
        
    ), 

], 
   id = 'sidebar', 
   className = SIDEBAR_STYLE, 
)

app.layout = html.Div([
    dcc.Store(id = 'side_click'),
    dcc.Location(id='url', refresh=False),
    navbar,
    sidebar,
    html.Div(id='page-content', children=[], className = CONTENT_STYLE )
])

#style = {'margin-left' : '18rem','margin-right': '2rem','padding':'2rem 1rem' }
@app.callback([
               Output('sidebar', 'style'),
               Output('page-content', 'style'),
               Output('side_click', 'data'),
               
               ],
              [Input('btn_sidebar', 'n_clicks')],
              [State('side_click','data'),]

)

def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

@app.callback(
    [Output(f"{i}_link", "active") for i in alarms_list],
    [Input("url", "pathname")],
)

def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False, False, False
    return [pathname == f"/pages/{i}" for i in alarms_list]

@app.callback(Output("page-content", "children"), 
             [Input("url", "pathname")])

def display_page(pathname):
    if pathname == '/pages/obs_alarm':
        try:
            return obs_alarm.layout
        except:
            return html.Div([
            html.H1('404 Not Found', className = 'text-danger'),
            html.Hr(),
            html.P(f'No Obstacle Detected Alarms from {StartDate} to {EndDate}'),
        
         ],
        )
    if pathname == '/pages/op_alarm':
        try:
            return op_alarm.layout
        except:
            return html.Div([
            html.H1('404 Not Found', className = 'text-danger'),
            html.Hr(),
            html.P(f'No Opening Time Alarms from {StartDate} to {EndDate}'),
        
         ],
        )
    if pathname == '/pages/cl_alarm':
        try:
            return cl_alarm.layout
        except:
            return html.Div([
            html.H1('404 Not Found', className = 'text-danger'),
            html.Hr(),
            html.P(f'No Closing Time Alarms from {StartDate} to {EndDate}'),
        
         ],
        )
    if pathname == '/pages/prise_alarm':
        try:
            return prise_alarm.layout
        except:
            return html.Div([
            html.H1('404 Not Found', className = 'text-danger'),
            html.Hr(),
            html.P(f'No Pressure Rise Alarms from {StartDate} to {EndDate}'),
        
         ],
        )
    if pathname == '/pages/pfall_alarm':
        try:
            return pfall_alarm.layout
        except:
            return html.Div([
            html.H1('404 Not Found', className = 'text-danger'),
            html.Hr(),
            html.P(f'No Pressure Fall Alarms from {StartDate} to {EndDate}'),
        
         ],
        )
    else:
        return html.Div([
            html.H1('404 Not Found', className = 'text-danger'),
            html.Hr(),
            html.P(f'The pathname {pathname} was not recognised...'),
        
         ],
        )


if __name__ == '__main__':
    print ('Run Run Run')
    app.run_server(host='0.0.0.0',port=8050,debug=True,use_reloader = False)
    

# In[ ]:




