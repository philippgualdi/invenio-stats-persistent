# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-persistent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for collecting statistics and save persistent in the database."""

from invenio_i18n import gettext as _

from . import config


class InvenioStatsPersistent(object):
    """invenio-stats-persistent extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-stats-persistent"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("PERSISTENT_STATS_"):
                app.config.setdefault(k, getattr(config, k))
