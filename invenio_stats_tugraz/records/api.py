# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2021 Graz University of Technology.
#
# Invenio-Records-Marc21 is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Statistic Api."""

from __future__ import absolute_import, print_function

from .dumpers import TugrazStatisticsDumperExt
from .systemfields.statistics import Marc21Statistics


class Marc21StatisticsDumperExt(TugrazStatisticsDumperExt):
    """Marc21 statistics dumper class."""

    def __init__(self, target_field="stats", api=Marc21Statistics):
        """Constructor.

        :param target_field: dot separated path where to dump the tokens.
        """
        super().__init__(target_field=target_field, api=api)
