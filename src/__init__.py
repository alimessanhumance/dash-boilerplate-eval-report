from flask import Flask
from flask_assets import Environment
from flask_session import Session


def create_app() -> Flask:
    """Create and configure the Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize plugins
    init_assets(app)
    init_session(app)

    with app.app_context():
        # Register routes
        from . import routes  # noqa

        # Initialize and register Dash app
        from .dashboard import init_dashboard
        app = init_dashboard(app)

    return app


def init_assets(app: Flask) -> None:
    """Initialize Flask-Assets."""
    assets = Environment()
    assets.init_app(app)


def init_session(app: Flask) -> None:
    """Initialize Flask-Session."""
    Session(app)
