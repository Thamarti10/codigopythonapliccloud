import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from models import db, Sale, Product
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Relatório de Vendas"),
    dcc.Graph(id='sales-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # Atualiza a cada 5 segundos
        n_intervals=0
    )
])

@app.callback(
    Output('sales-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    sales = Sale.query.all()
    data = []

    for sale in sales:
        data.append({
            'Produto': sale.product.name,
            'Quantidade': sale.quantity,
            'Data': sale.sale_date
        })

    df = pd.DataFrame(data)

    if not df.empty:
        fig = go.Figure([go.Bar(x=df['Produto'], y=df['Quantidade'])])
        return fig
    return {}

if __name__ == '__main__':
    app.run_server(debug=True)
