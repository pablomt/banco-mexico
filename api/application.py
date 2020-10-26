"""In this file it will be creating the context of the current FlaskAPI environment
"""
from logging.config import dictConfig

from flask_api import FlaskAPI
from flask_cors import CORS

def create_app(debug:bool = False, **config_overrides) -> FlaskAPI:
    """Handle the Flask API environment creation

    Defines all the context that includes the registation of the blueprints

    Args:
        debug (boolean): Defines if the current instance is on development or staging phase

    Return
        FlaskAPI - Returns the new instance of the application and environment
    """
    # Logger level
    logger_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }
        },
        'root': {
            'handlers': ['wsgi']
        }
    }

    if debug:
        logger_config['root']['level'] = 'DEBUG'
    elif testing:
        logger_config['root']['level'] = 'INFO'
    else:
        logger_config['root']['level'] = 'WARNING'

    # Application creation
    app = FlaskAPI(__name__, static_url_path='')

    # CORS Configuration, in prod and stage envs
    # defines the origins that can access to the api
    CORS(app, resources={r'/*': {"origins": "*"} })

    # Set config environment
    app.debug = debug
    app.testing = testing

    # Define parser for the response of requests
    app.config['DEFAULT_PARSERS'] = ['flask_api.parsers.JSONParser']

    # Add all configurations that had been sent
    app.config.from_pyfile('config.py')

    # Apply overrides for tests
    app.config.update(config_overrides)

    # Blueprints registration
    #from banxico.endpoints import udis_serie_app
    #from banxico.endpoints import usdmx_serie_app

    #app.register_blueprint(mongo_app, url_prefix='')
    #app.register_blueprint(udis_serie, url_prefix='/api/v1')
    #app.register_blueprint(usdmx_serie_app, url_prefix='/api/v1')

    return app