# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-stats-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Tugraz Celery tasks."""

from datetime import datetime, timedelta
from functools import partial

from invenio_access.permissions import system_identity
from invenio_search.engine import dsl
from invenio_search.proxies import current_search_client
from invenio_search.utils import prefix_index
from invenio_stats.bookmark import BookmarkAPI


def tugraz_reindex_stats(bookmark_name, stats_indices, service):
    """Reindex the documents where the stats have changed."""
    bm = BookmarkAPI(current_search_client, bookmark_name, "day")
    last_run = bm.get_bookmark()
    if not last_run:
        # If this is the first time that we run, let's do it for the documents of the last week
        last_run = (datetime.utcnow() - timedelta(days=7)).isoformat()
    reindex_start_time = datetime.utcnow().isoformat()
    indices = ",".join(map(lambda x: prefix_index(x) + "*", stats_indices))

    all_parents = set()
    query = dsl.Search(
        using=current_search_client,
        index=indices,
    ).filter({"range": {"updated_timestamp": {"gte": last_run}}})

    for result in query.scan():
        parent_id = result.parent_recid
        all_parents.add(parent_id)

    if all_parents:
        all_parents_list = list(all_parents)
        step = 10000
        end = len(list(all_parents))
        for i in range(0, end, step):
            records_q = dsl.Q("terms", parent__id=all_parents_list[i : i + step])
            service.reindex(
                params={"allversions": True},
                identity=system_identity,
                search_query=records_q,
            )
    bm.set_bookmark(reindex_start_time)
    return "%d documents reindexed" % len(all_parents)


marc21_stats_reindex = partial(tugraz_reindex_stats, "marc21_stats_reindex")
