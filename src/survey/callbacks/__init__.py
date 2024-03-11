from src.survey.callbacks.translate_content import translate_content


def init_callbacks(dash_app, translation_file):
    translate_content(dash_app, translation_file)
