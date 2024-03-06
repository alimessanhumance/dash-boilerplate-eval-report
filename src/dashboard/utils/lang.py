import json

from config import Config


def load_translation_file():
    with open(Config.TRANSLATION_FILE, "r", encoding="utf8") as json_file:
        translation = json.loads(json_file.read())

    return translation
