# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for collecting statistics for TU Graz."""

from invenio_i18n import gettext as _

from . import config


class InvenioStatsTugraz(object):
    """invenio-stats-tugraz extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self._app = app
        self.init_config(app)
        self.init_statistics(app)
        app.extensions["invenio-stats-tugraz"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        for k in dir(config):
            if k.startswith("TUGRAZ_"):
                app.config.setdefault(k, getattr(config, k))

    def init_statistics(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        events = app.config["TUGRAZ_STATS_EVENTS"]
        celery_jobs = app.config["TUGRAZ_CELERY_BEAT_SCHEDULE"]
        aggregations = app.config["TUGRAZ_STATS_AGGREGATIONS"]
        queries = app.config["TUGRAZ_STATS_QUERIES"]

        if "STATS_EVENTS" in app.config:
            app.config["STATS_EVENTS"].update(events)
        else:
            app.config["STATS_EVENTS"] = events

        if "CELERY_BEAT_SCHEDULE" in app.config:
            app.config["CELERY_BEAT_SCHEDULE"].update(celery_jobs)
        else:
            app.config["CELERY_BEAT_SCHEDULE"] = celery_jobs

        if "STATS_AGGREGATIONS" in app.config:
            app.config["STATS_AGGREGATIONS"].update(aggregations)
        else:
            app.config["STATS_AGGREGATIONS"] = aggregations

        if "STATS_QUERIES" in app.config:
            app.config["STATS_QUERIES"].update(queries)
        else:
            app.config["STATS_QUERIES"] = queries
