import os
from flask import Flask
from config import config_by_name

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG') or 'default'

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Import routes après création de l'app pour éviter circular import
    from . import routes
    routes.init_routes(app)  # Appelle la fonction qui enregistre les routes

    return app

# Définir app pour Gunicorn
app = create_app()
