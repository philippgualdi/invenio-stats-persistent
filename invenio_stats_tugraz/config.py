# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for collecting statistics for TU Graz."""

###### Statistics ###################
################################################

from datetime import timedelta

from celery.schedules import crontab
from invenio_stats.aggregations import StatAggregator
from invenio_stats.contrib.event_builders import build_file_unique_id
from invenio_stats.processors import EventsIndexer, anonymize_user, flag_robots
from invenio_stats.queries import TermsQuery

from .utils import build_record_unique_id

TUGRAZ_CELERY_BEAT_SCHEDULE = {
    # indexing of statistics events & aggregations
    "tugraz-stats-process-events": {
        "task": "invenio_stats.tasks.process_events",
        "args": [("marc21-record-view", "marc21-file-download")],
        "schedule": timedelta(minutes=1),  # Every hour at minute 25 and 55
    },
    "tugraz-stats-aggregate-events": {
        "task": "invenio_stats.tasks.aggregate_events",
        "args": [
            (
                "marc21-record-view-agg",
                "marc21-file-download-agg",
            )
        ],
        "schedule": timedelta(minutes=1),  # Every hour at minute 0
    },
    "marc21-reindex-stats": {
        "task": "invenio_records_marc21.services.tasks.marc21_reindex_stats",
        "args": [
            (
                "stats-marc21-record-view",
                "stats-marc21-file-download",
            )
        ],
        "schedule": crontab(minute=1),
    },
}

# Invenio-Stats
# =============
# See https://invenio-stats.readthedocs.io/en/latest/configuration.html

TUGRAZ_STATS_EVENTS = {
    "marc21-file-download": {
        "templates": "invenio_stats_tugraz.records.statistics.templates.events.marc21_file_download",
        "event_builders": [
            "invenio_rdm_records.resources.stats.file_download_event_builder",
            "invenio_rdm_records.resources.stats.check_if_via_api",
        ],
        "cls": EventsIndexer,
        "params": {
            "preprocessors": [flag_robots, anonymize_user, build_file_unique_id]
        },
    },
    "marc21-record-view": {
        "templates": "invenio_stats_tugraz.records.statistics.templates.events.marc21_record_view",
        "event_builders": [
            "invenio_rdm_records.resources.stats.record_view_event_builder",
            "invenio_rdm_records.resources.stats.check_if_via_api",
            "invenio_rdm_records.resources.stats.drop_if_via_api",
        ],
        "cls": EventsIndexer,
        "params": {
            "preprocessors": [flag_robots, anonymize_user, build_record_unique_id],
        },
    },
}

TUGRAZ_STATS_AGGREGATIONS = {
    "marc21-file-download-agg": {
        "templates": "invenio_stats_tugraz.records.statistics.templates.aggregations.aggr_marc21_file_download",
        "cls": StatAggregator,
        "params": {
            "event": "marc21-file-download",
            "field": "unique_id",
            "interval": "day",
            "index_interval": "month",
            "copy_fields": {
                "file_id": "file_id",
                "file_key": "file_key",
                "bucket_id": "bucket_id",
                "recid": "recid",
                "parent_recid": "parent_recid",
            },
            "metric_fields": {
                "unique_count": (
                    "cardinality",
                    "unique_session_id",
                    {"precision_threshold": 1000},
                ),
                "volume": ("sum", "size", {}),
            },
        },
    },
    "marc21-record-view-agg": {
        "templates": "invenio_stats_tugraz.records.statistics.templates.aggregations.aggr_marc21_record_view",
        "cls": StatAggregator,
        "params": {
            "event": "marc21-record-view",
            "field": "unique_id",
            "interval": "day",
            "index_interval": "month",
            "copy_fields": {
                "recid": "recid",
                "parent_recid": "parent_recid",
                "via_api": "via_api",
            },
            "metric_fields": {
                "unique_count": (
                    "cardinality",
                    "unique_session_id",
                    {"precision_threshold": 1000},
                ),
            },
            "query_modifiers": [lambda query, **_: query.filter("term", via_api=False)],
        },
    },
}

TUGRAZ_STATS_QUERIES = {
    "marc21-record-view": {
        "cls": TermsQuery,
        "permission_factory": None,
        "params": {
            "index": "stats-marc21-record-view",
            "doc_type": "marc21-record-view-day-aggregation",
            "copy_fields": {
                "recid": "recid",
                "parent_recid": "parent_recid",
            },
            "query_modifiers": [],
            "required_filters": {
                "recid": "recid",
            },
            "metric_fields": {
                "views": ("sum", "count", {}),
                "unique_views": ("sum", "unique_count", {}),
            },
        },
    },
    "marc21-record-view-all-versions": {
        "cls": TermsQuery,
        "permission_factory": None,
        "params": {
            "index": "stats-marc21-record-view",
            "doc_type": "marc21-record-view-day-aggregation",
            "copy_fields": {
                "parent_recid": "parent_recid",
            },
            "query_modifiers": [],
            "required_filters": {
                "parent_recid": "parent_recid",
            },
            "metric_fields": {
                "views": ("sum", "count", {}),
                "unique_views": ("sum", "unique_count", {}),
            },
        },
    },
    "marc21-record-download": {
        "cls": TermsQuery,
        "permission_factory": None,
        "params": {
            "index": "stats-marc21-file-download",
            "doc_type": "marc21-file-download-day-aggregation",
            "copy_fields": {
                "recid": "recid",
                "parent_recid": "parent_recid",
            },
            "query_modifiers": [],
            "required_filters": {
                "recid": "recid",
            },
            "metric_fields": {
                "downloads": ("sum", "count", {}),
                "unique_downloads": ("sum", "unique_count", {}),
                "data_volume": ("sum", "volume", {}),
            },
        },
    },
    "marc21-record-download-all-versions": {
        "cls": TermsQuery,
        "permission_factory": None,
        "params": {
            "index": "stats-marc21-file-download",
            "doc_type": "marc21-file-download-day-aggregation",
            "copy_fields": {
                "parent_recid": "parent_recid",
            },
            "query_modifiers": [],
            "required_filters": {
                "parent_recid": "parent_recid",
            },
            "metric_fields": {
                "downloads": ("sum", "count", {}),
                "unique_downloads": ("sum", "unique_count", {}),
                "data_volume": ("sum", "volume", {}),
            },
        },
    },
}
