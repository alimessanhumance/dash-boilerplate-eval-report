import json

from config import Config

TRANSLATION_FILES_MAP = {
    "home": Config.HOME_TRANSLATION_FILE,
    "survey": Config.SURVEY_TRANSLATION_FILE
}


def load_translation_file(app_name):
    with open(TRANSLATION_FILES_MAP[app_name], "r", encoding="utf8") as json_file:
        translation = json.loads(json_file.read())

    return translation
