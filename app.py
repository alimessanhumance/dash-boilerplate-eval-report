from config import Config
from src import create_app


def run_server():
    """Run the Flask server."""
    app = create_app()
    app.run(host="0.0.0.0", port=Config.SERVICE_PORT, debug=Config.FLASK_DEBUG)


if __name__ == "__main__":
    run_server()
