# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
# # Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Statistics integration for Tugraz records."""

from .api import LomStatistics, Marc21Statistics

__all__ = (
    "Marc21Statistics",
    "LomStatistics",
)
