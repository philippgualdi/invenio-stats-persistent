# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Utils module."""


def build_record_unique_id(doc):
    """Build record unique identifier."""
    doc["unique_id"] = "{0}_{1}".format(doc["recid"], doc["parent_recid"])
    return doc
