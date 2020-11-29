import logging

from smartcity.db import region_stats_collection
from smartcity.create_pdf import create_plot

logger = logging.getLogger(__name__)


def get_available_stats_list():
    db_resp = region_stats_collection.find({}, {"tag": 1, "title": 1})
    tags_list = [{"tag": d["tag"], "title": d["title"]} for d in db_resp]
    logger.info(f"Found available stats tags in DB: {tags_list}")
    return tags_list


def get_stats(stats_tag):
    res = region_stats_collection.find_one({"tag": stats_tag})
    if not res:
        raise ValueError(f"Not found stats with tag {stats_tag}")
    del res["_id"]
    logger.debug(f"Found stats table {res}")
    return res


def get_pdf(stats_tag):
    data = get_stats(stats_tag)
    logger.debug("Converting to PDF")
    create_plot(data)