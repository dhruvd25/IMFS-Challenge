import dash
import dash_html_components as html
import dash_core_components as dcc
from utils.dbutils import *
from utils.apphelper import *
import dash_table as dt
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

query_all_dates = """SELECT DISTINCT date from historical_price"""
all_dates = fetch(query_all_dates, fetch_type='all')[0]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dropdown = html.Div([
    html.Label('Dates'),
    dcc.Dropdown(
        id='dates-dropdown',
        options=[
            {'label': i[0], 'value':i[0]} for i in all_dates
        ],
        value='2020-12-31',
        multi=False
    ),
])

final_table = html.Div(id="final_table")


index_cal, columns = get_total_index()
cols = ['Date', 'Index Open', 'Index Close']
df = pd.DataFrame(index_cal, columns=cols)
fig_timeline = px.line(df, x='Date',y=['Index Close','Index Open'],
                       title='Index Value Timeline')

fig_timeline.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# bar_plot = html.Div(Dccid='bar_plot')

app.layout = html.Div(children=[
    html.H1(children='Price Weighted Index Overview'),
    html.Div(children='Total Index View'),
    dcc.Graph(figure=fig_timeline),
    html.Div(children='Historical Index View'),
    dropdown,
    final_table,
    html.Div(children='Sector Breakdown for Index'),
    dcc.Graph(id="bar_plot")
]
)


@app.callback(
    dash.dependencies.Output('final_table', 'children'),
    [dash.dependencies.Input('dates-dropdown', 'value')])
def update_output(value):

    table_values = [get_index_open_close(value)]

    dtable = dt.DataTable(
        id = 'table',
        columns = [{"name": "Index Open", "id": "Index Open"},
                 {"name": "Index Close", "id": "Index Close"},
                 {"name": "Average Volume", "id": "Average Volume"}],
        data = table_values)
    return [dtable]


@app.callback(
    dash.dependencies.Output('bar_plot', 'figure'),
    [dash.dependencies.Input('dates-dropdown', 'value')])
def update_output(value):

    graph_data = return_sector_open_close_volume(value)
    # for i in value:
    #     graph_data += return_sector_open_close_volume(i)
    cols = ['Date', 'Sector', 'Sector Open', 'Sector Close', 'Avg Vol']
    df = pd.DataFrame(graph_data, columns=cols)
    df.fillna('None', inplace=True)
    fig = px.pie(df,
                 names='Sector',
                 values='Sector Close',
                 color='Sector')
    return fig


if __name__ == '__main__':
    app.run_server()
