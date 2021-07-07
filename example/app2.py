import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app = dash.Dash()  # external_stylesheets=[dbc.themes.BOOTSTRAP]

app.layout = dbc.Container(
    [
        html.Div(
            dt.DataTable(
                id="table",
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
            ),
            className="db-thead-light",
        ),
        dbc.Table.from_dataframe(df, className="my-3 thead-dark"),
    ],
    className="dash-bootstrap p-2",
)

if __name__ == "__main__":
    app.run_server(debug=True)
