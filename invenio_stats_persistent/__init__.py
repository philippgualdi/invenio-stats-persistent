# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-persistent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for collecting statistics and save persistent in the database."""

from .ext import InvenioStatsPersistent

__version__ = "0.1.0"

__all__ = ("__version__", "InvenioStatsPersistent")
