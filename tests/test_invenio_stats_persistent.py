# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-persistent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_stats_persistent import InvenioStatsPersistent


def test_version():
    """Test version import."""
    from invenio_stats_persistent import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioStatsPersistent(app)
    assert "invenio-stats-persistent" in app.extensions

    app = Flask("testapp")
    ext = InvenioStatsPersistent()
    assert "invenio-stats-persistent" not in app.extensions
    ext.init_app(app)
    assert "invenio-stats-persistent" in app.extensions
