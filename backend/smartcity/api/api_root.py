import logging

import smartcity
from flask import request
from flask_restplus import Api, Resource, fields

from smartcity.business import get_stats

logger = logging.getLogger(__name__)

api = Api(title="smartcity API", version="1.0", description="Shifty API")


@api.route("/version")
class VersionResource(Resource):
    @api.response(200, "Success")
    @api.response(500, "Internal Error")
    def get(self):
        """
        Get backend and model version info and status
        :return:
        """
        resp = {"status": "Success", "version": smartcity.__version__}

        return resp, 200


@api.route("/stats")
class CommentPredict(Resource):
    @api.response(200, "Success")
    @api.response(400, "Validation Error")
    @api.response(500, "Internal Error")
    def post(self):
        """
        Make prediction for a single profile
        :return:
        """

        logger.info(f'Stats requested')
        resp = get_stats()

        resp.update({"status": "Success"})
        return resp, 200
