import dash_bootstrap_components as dbc
from dash import html
import dash


def navigation_layout():
    layout = dbc.Navbar(
        [
            html.A(
                # Use a logo or text as the brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src=dash.get_asset_url("img/LOGO_Humance_01.png"),
                                style={"height": "30px", "margin": "5px"}
                            ),
                            width=20,
                            style={"margin": "5px"}
                        ),
                    ]
                ),
                href="www.humance.ca",
            ),
            dbc.DropdownMenu(
                id="nav-lang-dropdown",
                children=[
                    dbc.DropdownMenuItem("English", id="en-lang"),
                    dbc.DropdownMenuItem("Français", id="fr-lang"),
                ],
                nav=True,
                in_navbar=True,
                label="Language",
                className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
                style={
                    "padding": "10px",
                    "color": "lightyellow"
                }
            )
        ],
        color="#383838",
        dark=True,  # Set to True for a dark navbar, False for a light navbar
    )

    return layout
