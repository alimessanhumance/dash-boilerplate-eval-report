import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from src.dashboard.templates.navigation_bar import navigation_layout
from src.dashboard.templates.home import home_layout

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
            dbc.themes.BOOTSTRAP
        ],
        suppress_callback_exceptions=True
    )
    dash_app.title = "Pixonality Data Interface"

    # Create dash app layout
    dash_app.layout = html.Div(
        children=[
            html.Div(children=navigation_layout()),
            html.Div(id="content"),
            dcc.Store(id="data"),
            dcc.Store(id="translation", data="en"),
            dcc.Location(id="url", refresh=False),
        ],
    )

    # Initialize callbacks after our app is loaded
    init_callbacks(dash_app)

    return dash_app.server


def init_callbacks(dash_app):

    @dash_app.callback(
        [
            Output("content", "children"),
            Output("en-lang", "n_clicks"),
            Output("fr-lang", "n_clicks"),
            Output("translation", "data")
        ],
        [
            Input("en-lang", "n_clicks"),
            Input("fr-lang", "n_clicks"),
            Input("url", "pathname")
        ],
        [
            State("translation", "data")
        ]
    )
    def translate_content(en, fr, url, lang):
        """
        Render translated layout
        """

        ctx = dash.callback_context

        # If the callback was triggered by the "url" input
        if ctx.triggered[0]["prop_id"] == "url.pathname":

            return [home_layout(translations[lang]), None, None, lang]

        # If the callback was triggered by the "en-lang" or "fr-lang" input
        else:

            # Select french if clicked
            if fr:
                lang = "fr"
            else:
                lang = "en"  # Default

            # Return layout and reset n_clicks
            return [home_layout(translations[lang]), None, None, lang]
