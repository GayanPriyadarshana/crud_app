import dash
from dash import Input, Output, State, dcc, html, dash_table
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        dcc.Input(
            id='adding-columns-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='adding-columns-button', n_clicks=0)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='our-table',
        columns=[
            {'name': 'Product', 'id': 'Product', 'deletable': False, 'renamable': False},
            {'name': 'Version', 'id': 'Version', 'deletable': True, 'renamable': True},
            {'name': 'Price', 'id': 'Price', 'deletable': True, 'renamable': True},
            {'name': 'Sales', 'id': 'Sales', 'deletable': False, 'renamable': False}
        ],
        data=[
            {'Product': 'Iphone', 'Version': '6a', 'Price': 799, 'Sales': 2813},
            {'Product': 'Iphone', 'Version': '9', 'Price': 900, 'Sales': 5401},
            {'Product': 'Iphone', 'Version': '7', 'Price': 799, 'Sales': 2513},
            {'Product': 'Iphone', 'Version': '8', 'Price': 850, 'Sales': 5401},
            {'Product': 'Galaxy', 'Version': 'S9', 'Price': 900, 'Sales': 6084},
            {'Product': 'Galaxy', 'Version': 'S10', 'Price': 1000, 'Sales': 7084},
            {'Product': 'Galaxy', 'Version': 'S20', 'Price': 1200, 'Sales': 9084},
            {'Product': 'Pixel', 'Version': '1', 'Price': 400, 'Sales': 2084},
            {'Product': 'Pixel', 'Version': '2', 'Price': 500, 'Sales': 3033},
            {'Product': 'Pixel', 'Version': '3', 'Price': 600, 'Sales': 6000},
        ],
        editable=True,
        row_deletable=True,
        sort_action='native',
        sort_mode='single',
        filter_action='native',
        page_action='none',
        style_table={'height': '300px', 'overflowY': 'auto'},
        style_cell={'textAlign': 'left', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'right'
            } for c in ['Price', 'Sales']
        ]
    ),

    html.Button('Add Row', id='editing-rows-button', n_clicks=0),
    html.Button('Export to Excel', id='save_to_csv', n_clicks=0),

    # Create notification when saving to excel
    html.Div(id='placeholder', children=[]),
    dcc.Store(id='store', data=0),
    dcc.Interval(id='interval', interval=1000),

    dcc.Graph(id='my_graph')
])

@app.callback(
    Output('our-table', 'columns'),
    [Input('adding-columns-button', 'n_clicks')],
    [State('adding-columns-name', 'value'),
     State('our-table', 'columns')]
)

def add_column(n_clicks, value, existing_columns):
    print(existing_columns)
    if n_clicks > 0:
        existing_columns.append({
            'name': value, 'id': value,
            'renamable': True, 
        })
    print(existing_columns)
    return existing_columns


if __name__ == '__main__':
    app.run_server(debug=True)