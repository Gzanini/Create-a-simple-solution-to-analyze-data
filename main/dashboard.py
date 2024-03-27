import dash
from dash import html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Carregar os dados
caminho_arquivo = 'ControleGastos - 2024.xlsx'
mov_cartao = pd.read_excel(caminho_arquivo, sheet_name='Mov_cartao', usecols="A:I")

# Convertendo colunas para o tipo correto
mov_cartao['Ano'] = mov_cartao['Ano'].astype(str)
mov_cartao['Mês'] = mov_cartao['Mês'].astype(str)
mov_cartao['Valor'] = pd.to_numeric(mov_cartao['Valor'], errors='coerce')

# Preparando as opções de seleção para Ano e Mês
anos_disponiveis = sorted(mov_cartao['Ano'].unique())
opcoes_ano = [{'label': ano, 'value': ano} for ano in anos_disponiveis]

meses_disponiveis = sorted(mov_cartao['Mês'].unique(), key=lambda x: int(x))
opcoes_mes = [{'label': mes, 'value': mes} for mes in meses_disponiveis]

app.layout = html.Div([
    html.H1('Dashboard de Análise de Gastos', style={'textAlign': 'center'}),

    html.Div([
        html.Div("Selecione o Ano:", style={'marginRight': '10px', 'display': 'inline-block'}),
        dcc.Dropdown(
            id='seletor-ano',
            options=opcoes_ano,
            value=anos_disponiveis[0],
            clearable=False,
            style={'width': '200px', 'display': 'inline-block'}
        ),
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),

    dcc.Graph(id='grafico-anual'),

    html.Div([
        html.Div("Selecione o Mês:", style={'marginRight': '10px', 'display': 'inline-block'}),
        dcc.Dropdown(
            id='seletor-mes',
            options=opcoes_mes,
            value=meses_disponiveis[0],
            clearable=False,
            style={'width': '200px', 'display': 'inline-block'}
        ),
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),

    dcc.Graph(id='grafico-mensal'),
    html.Div(id='tabela-gastos'),
])


@app.callback(
    Output('grafico-anual', 'figure'),
    Input('seletor-ano', 'value')
)
def atualizar_grafico_anual(ano_selecionado):
    filtro = mov_cartao['Ano'] == ano_selecionado
    df_filtrado = mov_cartao[filtro]
    df_ordenado = df_filtrado.sort_values(by='Valor', ascending=False)
    fig = px.bar(df_ordenado, x='Categoria', y='Valor', color='Categoria',
                 title=f'Gastos Anuais por Categoria - {ano_selecionado}')
    return fig


@app.callback(
    [Output('grafico-mensal', 'figure'),
     Output('tabela-gastos', 'children')],
    [Input('seletor-mes', 'value'),
     Input('seletor-ano', 'value')]
)
def atualizar_grafico_mensal(mes_selecionado, ano_selecionado):
    filtro = (mov_cartao['Mês'] == mes_selecionado) & (mov_cartao['Ano'] == ano_selecionado)
    df_filtrado = mov_cartao[filtro]
    df_ordenado = df_filtrado.sort_values(by='Valor', ascending=False)
    fig = px.bar(df_ordenado, x='Categoria', y='Valor', color='Categoria',
                 title=f'Gastos do Mês {mes_selecionado} por Categoria - {ano_selecionado}')

    # Gastos por cartão
    gastos_por_cartao = df_filtrado.groupby('Cartao')['Valor'].sum().reset_index()
    total = pd.DataFrame([{'Cartao': 'Total', 'Valor': gastos_por_cartao['Valor'].sum()}])
    gastos_por_cartao = pd.concat([gastos_por_cartao, total], ignore_index=True)
    tabela = dash_table.DataTable(
        data=gastos_por_cartao.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in gastos_por_cartao.columns],
        style_as_list_view=True,
        style_cell={'padding': '5px'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
            }
        ]
    )

    return fig, tabela


if __name__ == '__main__':
    app.run_server(debug=True)
