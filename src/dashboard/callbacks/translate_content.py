from dash.dependencies import Input, Output, State

from src.dashboard.templates.home import home_layout
from src.dashboard.utils.lang import load_translation_file

translations = load_translation_file()


def translate_content(dash_app):
    @dash_app.callback(
        [
            Output("body", "children"),
            Output("en-lang", "n_clicks"),
            Output("fr-lang", "n_clicks"),
            Output("dash-lang", "data")
        ],
        [
            Input("en-lang", "n_clicks"),
            Input("fr-lang", "n_clicks"),
        ],
        [
            State("dash-lang", "data")
        ],
        prevent_initial_call=True
    )
    def callback(en, fr, lang):
        """
        Render translated layout
        """

        # Select french if clicked
        if fr:
            lang = "fr"
        else:
            lang = "en"  # Default

        # Return layout and reset n_clicks
        return [home_layout(translations[lang]), None, None, lang]
