import logging
import os

import smartcity
from flask import current_app
from smartcity.api import req_parsers
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
class StatsData(Resource):
    @api.response(200, "Success")
    @api.response(400, "Validation Error")
    @api.response(500, "Internal Error")
    def get(self):
        """
        Make prediction for a single profile
        :return:
        """

        logger.info(f'Stats requested')
        resp = get_stats()

        resp.update({"status": "Success"})
        return resp, 200


@api.route("/parser")
class ParserUpload(Resource):
    @api.response(200, "Success")
    @api.response(400, "Validation Error")
    @api.response(500, "Internal Error")
    @api.expect(req_parsers.file_upload)
    def post(self):
        """
        Make prediction for a single profile
        :return:
        """
        args = req_parsers.file_upload.parse_args()

        destination = os.path.join(current_app.config.get('UPLOAD_FILES_PATH'), 'parser_scripts/')
        os.makedirs(destination, exist_ok=True)

        file = args['script']
        filename = file.filename
        filepath = os.path.join(destination, filename)
        fileind = 0
        while os.path.exists(filepath):
            fileind += 1
            name, ext = os.path.splitext(filename)
            filepath = os.path.join(destination, f"{name}_({fileind}){ext}")

        logger.info(f'Saving file to {filepath}')
        file.save(filepath)

        resp = {"status": "Success"}
        return resp, 200
