import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1'),
        dcc.Tab(label='Tab 2', value='tab-2'),
    ]),
    dcc.Loading(
        id="loading",
        type="default",
        children=html.Div(id='tab-content'),
        style={'display': 'none'}
    )
])

@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dcc.Graph(id='graph-1')  # Placeholder for the first graph
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.Graph(id='graph-2')  # Placeholder for the second graph
        ])

@app.callback(
    Output('graph-1', 'figure'),
    Input('tabs', 'value')
    # prevent_initial_call=True
)
def update_graph_1(tab):
    if tab == 'tab-1':
        # Sample data for Graph 1
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='Sine Wave'))
        fig.update_layout(title='Sine Wave Graph')
        return fig

@app.callback(
    Output('graph-2', 'figure'),
    Input('tabs', 'value')
    # prevent_initial_call=True
)
def update_graph_2(tab):
    if tab == 'tab-2':
        # Sample data for Graph 2
        x = np.linspace(0, 10, 100)
        y = np.cos(x)
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='Cosine Wave'))
        fig.update_layout(title='Cosine Wave Graph')
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server(
                   port=8051, 
                   dev_tools_ui=True, 
                   dev_tools_hot_reload=True, 
                   threaded=True
                   )
