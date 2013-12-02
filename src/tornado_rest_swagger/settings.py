#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path

__author__ = 'flier'

SWAGGER_VERSION = '1.2'

URL_SWAGGER_API_DOCS = 'swagger-api-docs'
URL_SWAGGER_API_LIST = 'swagger-api-list'
URL_SWAGGER_API_SPEC = 'swagger-api-spec'

ASSETS_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'assets')
DEFAULT_LOGGING_FORMAT = "%(asctime)s\t%(levelname)s [%(process)d:%(threadName)s]\t<%(name)s> %(message)s"

default_settings = {
    'base_url': '/',
    'assets_path': ASSETS_PATH,

    'api_version': '0.2.2',
    'api_key': '',
    'enabled_methods': ['get', 'post', 'put', 'delete'],
    'exclude_namespaces': [],
}
