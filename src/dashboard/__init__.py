from flask import session

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from src.dashboard.templates.navigation_bar import navigation_layout
from src.dashboard.templates.home import home_layout

from src.dashboard.callbacks import init_callbacks

from src.dashboard.utils.lang import load_translation_file

translations = load_translation_file()


# Initializing dash application
def init_dashboard(flask_app):
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        serve_locally=True,  # To prevent serving dash dependencies from CDN so we can better control versions
        routes_pathname_prefix=flask_app.config["DASH_APP_BASE_URL"],
        update_title=None,
        meta_tags=[
            # Additional meta tags
            {
                "name": "robots",
                "content": "noindex"
            }
        ],
        external_stylesheets=[
            # Custom fonts
            "https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400;1,700&display=swap",
            "https://www.w3schools.com/w3css/4/w3.css",
            dbc.themes.BOOTSTRAP
        ],
        suppress_callback_exceptions=True
    )
    dash_app.title = "Dash Boilerplate"
    dash_app._favicon = "favicon.png"

    def create_layout():
        lang = session.get("lang", "en")  # Default language is "en"
        return html.Div(
            children=[
                dcc.Store(id="data"),
                dcc.Store(id="dash-lang", data=lang),
                dcc.Location(id="url", refresh=False),
                html.Div(
                    id="content",
                    children=[
                        html.Div(id="navbar", children=navigation_layout()),
                        html.Div(id="body", children=home_layout(translations[lang]))
                    ]
                )
            ]
        )

    # Create dash app layout
    dash_app.layout = create_layout

    # Initialize callbacks after our app is loaded
    init_callbacks(dash_app)

    return dash_app.server
