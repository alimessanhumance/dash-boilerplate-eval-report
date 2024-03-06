from os import environ, path
from datetime import timedelta

from dotenv import load_dotenv


BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"), override=True)


class Config:
    # General flask config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = environ.get("FLASK_DEBUG") == "True"

    # Encrypted server flask_session config
    SESSION_PERMANENT = True
    SESSION_TYPE = "filesystem"
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SESSION_FILE_THRESHOLD = 100

    # Directories
    SRC_FOLDER = BASE_DIR + "/src"
    TEMP_FOLDER = BASE_DIR + "/temp"
    DASH_FOLDER = SRC_FOLDER + "/dashboard"
    FLASK_STATIC_FOLDER = SRC_FOLDER + "/static"
    DASH_STATIC_FOLDER = DASH_FOLDER + "/static"
    TEMPLATES_FOLDER = DASH_FOLDER + "/templates"
    TRANSLATION_FILE = DASH_STATIC_FOLDER + "/lang.json"

    # Our custom config
    SERVICE_NAME = environ.get("SERVICE_NAME")
    SERVICE_PORT = environ.get("SERVICE_PORT")

    DASH_APP_BASE_URL = environ.get("DASH_APP_BASE_URL")
