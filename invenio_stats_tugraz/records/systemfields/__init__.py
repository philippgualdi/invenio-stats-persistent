# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.


"""System fields module."""


from .statistics import LomRecordStatisticsField, Marc21RecordStatisticsField

__all__ = (
    "Marc21RecordStatisticsField",
    "LomRecordStatisticsField",
)
