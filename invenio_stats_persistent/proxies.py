# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-persistent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Helper proxy to the state object."""

from flask import current_app
from werkzeug.local import LocalProxy

current_statistics_persistent = LocalProxy(
    lambda: current_app.extensions["invenio-stats-persistent"]
)
"""Helper proxy to get the current tugraz statistics extension."""
