from datetime import timedelta
from flask import request, session, make_response, render_template, redirect
from flask import current_app as app


from src.home import init_dashboard as init_home_app
from src.survey import init_dashboard as init_survey_app
from src.utils.lang import get_user_lang


HOME_APP_PATH = app.config["DASH_APPS_BASE_URL"]
print(HOME_APP_PATH)

home_app = init_home_app(flask_app=app, name="home")
survey_app = init_survey_app(flask_app=app, name="survey")


@app.before_first_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)


@app.before_request
def before_request() -> None:
    """
    Global route guard.
    """

    if not request.path.startswith(HOME_APP_PATH):
        return  # Non-dash route

    # Main dash route
    if request.path == HOME_APP_PATH:
        session.clear()
        session["lang"] = get_user_lang(request)


@app.after_request
def after_request(response: make_response) -> make_response:
    """
    Global route cleanup.
    """
    if not request.path.startswith(HOME_APP_PATH):
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


# Home application
@app.route(HOME_APP_PATH + "/home/")
def render_home_page():
    return home_app.index()


@app.route(HOME_APP_PATH + "/home")
@app.route(HOME_APP_PATH + "/home/<path:something>")
def redirect_to_home_page():
    return redirect(HOME_APP_PATH + "/home/")


# Home application
@app.route(HOME_APP_PATH + "/survey/")
def render_survey_app():
    return survey_app.index()


# Interface redirection to report application
@app.route(HOME_APP_PATH + "/survey")
def redirect_to_survey():
    return redirect(HOME_APP_PATH + "/survey/")
