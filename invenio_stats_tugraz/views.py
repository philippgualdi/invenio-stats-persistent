# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for collecting statistics for TU Graz."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint
from invenio_i18n import gettext as _

blueprint = Blueprint(
    "invenio_stats_tugraz",
    __name__,
    template_folder="templates",
    static_folder="static",
)
