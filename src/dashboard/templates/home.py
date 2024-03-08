from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


def home_layout(translation):

    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Loading(
                                type="graph",
                                fullscreen=True,
                                children=html.H1(translation["title"], className="title"),
                                className="custom-loading"  # Adjust the opacity as needed
                            ),
                        ]
                    )
                ]
            )
        ]
    )
