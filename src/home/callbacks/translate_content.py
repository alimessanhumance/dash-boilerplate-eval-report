from dash.dependencies import Input, Output, State

from src.home.templates.home import home_layout


def translate_content(dash_app, translation_file):
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
        return [home_layout(translation_file[lang]), None, None, lang]
