"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        # Import main Blueprint
        from . import routes
        app.register_blueprint(routes.main_bp)

        # Import Dash application
        from .dashboards import apps
        app = apps.Add_Review_Dash(app)

        return app