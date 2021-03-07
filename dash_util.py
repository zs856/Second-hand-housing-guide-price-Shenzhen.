import dash
import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
def draw_graph(df):
    fig = px.scatter(df, x="项目名称", y="成交参考价格 \n（元/平方米）",
                     size="成交参考价格 \n（元/平方米）", color="行政区", hover_name="项目名称",
                     log_y=True)
    return fig
def run_server(df):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    fig = draw_graph(df)
    app.layout = html.Div(children=[
        html.H4(children='深圳二手房参考价(2021)'),
        generate_table(df,9999999999),
        dcc.Graph(
            id='可视化分析',
            figure=fig
        )
    ])
    app.run_server(debug=True)