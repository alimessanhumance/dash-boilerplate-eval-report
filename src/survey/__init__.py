from flask import session

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from src.utils.lang import load_translation_file
from src.common_dash.navigation_bar import navigation_layout
from src.survey.templates.slide import slide_layout
from src.survey.callbacks import init_callbacks


translations = load_translation_file(app_name="survey")


# Initializing dash application
def init_dashboard(flask_app, name):
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        serve_locally=True,  # To prevent serving dash dependencies from CDN so we can better control versions
        routes_pathname_prefix=f"{flask_app.config['DASH_APPS_BASE_URL']}/{name}/",
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
    dash_app.title = "Survey Boilerplate"
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
                        html.Div(id="body", children=slide_layout())
                    ]
                )
            ]
        )

    # Create dash app layout
    dash_app.layout = create_layout

    # Initialize callbacks after our app is loaded
    init_callbacks(dash_app, translation_file=translations)

    return dash_app.server
