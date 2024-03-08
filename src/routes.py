from flask import request, session, make_response, render_template
from flask import current_app as app

from src.utils.lang import get_user_lang

DASH_APP_PATH = app.config["DASH_APP_BASE_URL"]


@app.before_request
def before_request() -> None:
    """
    Global route guard.
    """

    if not request.path.startswith(DASH_APP_PATH):
        return  # Non-dash route

    # Main dash route
    if request.path == DASH_APP_PATH:
        session.clear()
        session["lang"] = get_user_lang(request)


@app.after_request
def after_request(response: make_response) -> make_response:
    """
    Global route cleanup.
    """
    if not request.path.startswith(DASH_APP_PATH):
        session.clear()

    # Response header to prevent embedding app inside any iframe
    response.headers["X-Frame-Options"] = "DENY"
    return response


@app.route("/health")
def health() -> make_response:
    """
    Health endpoint (for Kubernetes).
    """
    response = {
        "service": app.config["SERVICE_NAME"],
        "status": "UP",
    }
    return make_response(response, 200)


@app.errorhandler(404)
def not_found(err=None) -> make_response:
    """
    Handles not found errors (404 route).
    """
    lang = get_user_lang(request)

    if err is not None:
        print(err)

    return make_response(render_template(f"404/{lang}.jinja2"), 404)
