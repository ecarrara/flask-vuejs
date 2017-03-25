# -*- coding: utf-8 -*-

import os

VERSION = '0.0.1-unreleased'

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

DEBUG = ENVIRONMENT == 'development'

TESTING = ENVIRONMENT == 'testing'

SECRET_KEY = os.getenv('SECRET_KEY', u'Camarão bom é nascido em Cabrobó')

SENTRY_CONFIG = {
    'dsn': os.getenv('SENTRY_DSN'),
    'release': VERSION
}

JSONIFY_PRETTYPRINT_REGULAR = DEBUG
