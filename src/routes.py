from flask import request, session, make_response, render_template
from flask import current_app as app

from src.utils.lang import get_user_lang

DASH_APP_PATH = app.config["DASH_APP_BASE_URL"]


@app.before_request
def before_request() -> None:
    """
    Global route guard.
    """
    session.clear()
    session["lang"] = get_user_lang(request)
    if not request.path.startswith(DASH_APP_PATH):
        return  # Non-dash route

    # Main dash route
    # if request.path == DASH_APP_PATH:
        # session.clear()


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

    if err is not None:
        print(err)

    return make_response(render_template(f"404/{session['lang']}.jinja2"), 404)
