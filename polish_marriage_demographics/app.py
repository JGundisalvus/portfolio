from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Import Data
df_cmr = pd.read_csv(f'./polish_marriage_demographics/data/dash_data/crude_marriage_rate.csv', index_col=0)
df_avg_age = pd.read_csv(f'./polish_marriage_demographics/data/dash_data/average_marriage_age.csv', index_col=0)
df_marriage = pd.read_csv(f'./polish_marriage_demographics/data/dash_data/marriage_by_age_group.csv', index_col=0)
df_total_marriages = pd.read_csv(f'./polish_marriage_demographics/data/dash_data/total_marriages.csv', index_col=0)

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(style={'background':'white'}, children=[
    html.H1('Marriages in Poland by Age Group and Gender'),
    dcc.Tabs( id='main-tab', value='tab-total-marriages', children=[
        dcc.Tab(label='Total Marriages', value='tab-total-marriages'),
        dcc.Tab(label='Ave Age of Couple', value='tab-ave-age'),
        dcc.Tab(label='Marriages by Age Group', value='tab-age-groups'),
    ]
    ),
    dcc.Loading(
    id="loading",
    type="default",
    children=html.Div(id='tabs-content-graph'),
    style={'display': 'none'}  # Hides loading spinner
    )

])

# Callback on selecting a tab

@app.callback(
    Output('tabs-content-graph','children'),
    Input('main-tab','value')
)
def render_html(tab_value):
    
    if tab_value == 'tab-total-marriages':

        html_element = html.Div(children=[
                                html.H3('Total Marriages by Year'),
                                dcc.Dropdown(
                                    id='total-category-selector',
                                    options=[
                                        {'label': 'Total Marriages', 'value': 'total'},
                                        {'label': 'Crude Marriage Rate', 'value': 'cmr'}
                                    ],
                                    value='total',
                                    style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}
                                ),

                                dcc.Graph(id='tab-1-main-content'
                                )],
                                style={'padding': '50px'}
                                )
        
    elif tab_value == 'tab-ave-age':
        html_element = html.Div(children=[
                                html.H3('Ave Age of Bride and Grooms'),
                                dcc.Graph(id='tab-2-main-content')
                                ]
                                )
        
    elif tab_value == 'tab-age-groups':
        html_element = html.Div(children=[
                                html.H3('Number of Marriages by Age Group & Year'),
                                dcc.Dropdown(
                                    id='group-category-selector',
                                    options=[
                                        {'label': 'Total Marriages', 'value': 'total'},
                                        {'label': '% of Total Marraiges', 'value': 'per-total'}
                                    ],
                                    value='total',
                                    style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}
                                ),
                                dcc.Dropdown(
                                    id='gender-selector',
                                    options=[
                                        {'label': 'Women', 'value': 'female'},
                                        {'label': 'Men', 'value': 'male'},
                                        {'label': 'Both', 'value': 'both'}
                                    ],
                                    value='both',
                                    style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}
                                ),
                                dcc.Graph(id='tab-3-main-content')
                                ]
                                )
    return html_element

# If CMR is selected show EU CMR Option

# @app.callback(
#     Output('show-eu-cmr', 'style'),
#     [Input('total-category-selector', 'value'),
#     Input('show-eu-cmr', 'style')]
# )
# def toggle_eu_cmr_visibility(selected_value, current_style):
#     if current_style is None:
#         current_style = {}
#     current_style = current_style.copy()  # Make a copy to avoid mutating the original state

#     if selected_value != 'cmr':
#         current_style['display'] = 'none'
#     else:
#         current_style['display'] = 'block'
    
#     return current_style

# Render Graph for Tab 1
@app.callback(
    Output('tab-1-main-content', 'figure'),
    [Input('total-category-selector', 'value'),
    # Input('show-eu-cmr', 'value'),
    Input('main-tab', 'value')]
)
def tab_one_total_plots(total_type_value, tab_val):

    fig = make_subplots(specs=[[{"secondary_y": False}]])

    if total_type_value == 'total':
        df=df_total_marriages
        fig.add_trace(go.Scatter(x=df['Year'], y=df['Value'], name="Count of Marriages"), secondary_y=False,)
        return fig

    else:
        df = df_cmr
        fig.add_trace(go.Scatter(x=df['year'], y=df['cmr'], name="CMR of PL"), secondary_y=False,)
        fig.add_trace(go.Scatter(x=df['year'], y=df['cmr eu'], name="CMR of EU"), secondary_y=False,)
        
        # if cmr_value == 'eu-cmr':
        #     df=df_cmr.loc[:,['year', 'cmr eu']]
        #     fig.add_trace(go.Scatter(x=df['year'], y=df['cmr eu'], name="CMR of EU"), secondary_y=False,)
    
    return fig

# Render Graph for Tab 2
@app.callback(
    Output('tab-2-main-content','figure'),
    Input('main-tab','value'),
)
def tab_two_average_age_graph(tab_value):

    fig = make_subplots(specs=[[{"secondary_y": False}]])

    for gender in df_avg_age['gender'].unique():
        df = df_avg_age[df_avg_age['gender'] == gender]
        fig.add_trace(go.Scatter(x=df['year'], y=df['ave age'], name=f"Ave age of {gender}"), secondary_y=False)

    return fig

# Render graph for Tab 3
@app.callback(
    Output('tab-3-main-content', 'figure'),
    [Input('main-tab', 'value'),
     Input('group-category-selector', 'value'),
     Input('gender-selector', 'value')]
)
def tab_three_graphs(tab_value, group_value, gender_value):

    if gender_value == 'both':
        fig = make_subplots(rows=1, cols=2, subplot_titles=['men', 'women'])
        if group_value == 'total':

            for i, gender in enumerate(df_marriage['gender'].unique(),1):
                for age_group in df_marriage['age group'].unique():
                    df_temp = df_marriage[(df_marriage['age group'] == age_group) & (df_marriage['gender'] == gender )]
                    fig.add_trace(go.Scatter(x=df_temp['Year'], y=df_temp['Value'], mode='lines', name=f'{age_group} {gender}'), row=1, col=i)
                
            return fig
        else:
            return fig
        
    else:
        fig = go.Figure()

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(#mode='inline', 
                   port=8050, 
                   debug=True,
                   dev_tools_ui=True, 
                   dev_tools_hot_reload=True, 
                   threaded=True
                   )
