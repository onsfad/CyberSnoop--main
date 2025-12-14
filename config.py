import os

class Config:
    # Essential for security: Replace this with a long, random string in production
    # It is best practice to load this from an environment variable (e.g., os.environ.get('SECRET_KEY'))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-secret-key'

    # Database configuration (example for SQLAlchemy)
    # Replace with your actual database URI (e.g., PostgreSQL, MySQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other common settings
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    # Ensure DEBUG is False in production
    DEBUG = False
    # You might want to use a more robust database here
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass

# Dictionary to easily select the configuration based on an environment variable
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}