# -*- coding: utf-8 -*-

from flask import Flask, jsonify, g
from flask_cors.extension import CORS
from raven.contrib.flask import Sentry
from todolist.api import api
from todolist import config


def create_app():

    app = Flask(__name__)
    app.config.from_object(config)

    if app.config['ENVIRONMENT'] == 'production' and \
            app.config['SENTRY_CONFIG']['dsn']:
        Sentry(app)

    CORS(app)

    @app.errorhandler(500)
    def bad_things_happens(error):
        error_id = None
        if app.config['SENTRY_CONFIG']['dsn']:
            error_id = g.sentry_event_id

        return jsonify({
            'message': 'Internal server error.',
            'error_id': error_id
        })

    app.register_blueprint(api, url_prefix='/v0')

    return app
