# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_stats_tugraz import InvenioStatsTugraz


def test_version():
    """Test version import."""
    from invenio_stats_tugraz import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioStatsTugraz(app)
    assert "invenio-stats-tugraz" in app.extensions

    app = Flask("testapp")
    ext = InvenioStatsTugraz()
    assert "invenio-stats-tugraz" not in app.extensions
    ext.init_app(app)
    assert "invenio-stats-tugraz" in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert "Welcome to invenio-stats-tugraz" in str(res.data)
