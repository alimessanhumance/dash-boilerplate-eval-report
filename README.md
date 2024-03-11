# dash-boilerplate
Project structure that provides a foundation or starting point for a new Dash application project.

# Instructions
1. Clone the repository : `git clone https://github.com/aubertsigouin/dash-boilerplate`
2. Create a new virtual environment : `python -m venv venv`
3. Activate the virtual environment (Windows Git Bash) : `source venv/Scripts/activate`
4. Install dependecies : `pip install -r requirements.txt`
5. Edit the `.env` file and add environment variables specific to the project
6. Create mapping in `config.py` if variables are added at step 5. 
7. Create layouts, components, services, callbacks, etc. (Project-specific development)
8. Open the application : `python -m app`

# Tree structure
- dash-boilerplate
  - `app.py` : Start application
  - src
    - `__init__.py` : Create and configure Flask server
    - `routes.py` : Define Flask routes. Static data fetching should be done here in the before_request decorators. In this case, you would add a services folder or file.
    - templates : 404 jinja templates
    - utils
    - static : resources and styles for Flask templates
    - dashboard : Dash application
      - `__init__.py` : Create and configure Dash app
      - assets : resources and styles for Dash app
      - callbacks : Dash app callbacks
      - components : Dash app HTML components
      - services : API and DB wrappers for dynamic queries
      - static : translations
      - templates : Dash layouts and templates
      - utils

    
# Note
## Routes
Dash is responsible for routes inside the Dash app, defined in `.env`. The variable is `DASH_APP_BASE_URL=/app/` by default. Routes outside of Dash app are handled by Flask.

## Translation
There is no i8n/Babel/`.po`/`.mo`. For Flask templates, we avoid jinja `gettext` and we have one template for fr, one for en. Language for Flask templates is defined here : 
1. Prioritize lang parameter in request URL if available
2. Prioritize Accept-language in request header if available
3. Use `eng` as default

For Dash, we load a translation file located here : src/dashboard/static/`lang.json`. Dash components and layouts reference fields in this file.

## Before request
1. If actions are needed prior to render page, you should do it inside src/`routes.py` in the `before_request` function. For example, things such has user validation, static data fetching, routine tasks, session cache clearing.

# Where to go from here
1. Boilerplate for multiple Dash apps inside on Flask application
2. Boilerplate for creating and manage a local DB (users, view, etc.)
3. Boilerplate for authentication
4. Add logger
