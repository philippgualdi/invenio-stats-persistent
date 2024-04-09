# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Tugraz statistics module."""

from .api import Marc21StatisticsDumperExt
from .schema import TugrazStatisticSchema

__all__ = (
    "Marc21StatisticsDumperExt",
    "TugrazStatisticSchema",
)
