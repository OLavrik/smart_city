import logging

import yc_backend
from flask import request
from flask_restplus import Api, Resource, fields
from yc_backend.api.req_parsers import comment_predict_parser
from yc_backend.predict import predict

logger = logging.getLogger(__name__)

api = Api(title="yoloco-comments API", version="1.0", description="Shifty API")

req_item_predict = api.model(
    "Item to analyze",
    {
        "ID": fields.String,
        "USERNAME": fields.String,
        "BIOGRAPHY": fields.String,
        "FULL_NAME": fields.String,
        "LINK": fields.String,
    },
)

@api.route("/version")
class VersionResource(Resource):
    @api.response(200, "Success")
    @api.response(500, "Internal Error")
    def get(self):
        """
        Get backend and data version info and status
        :return:
        """
        resp = {"status": "Success", "version": yc_backend.__version__}

        return resp, 200


@api.route("/predict")
class CommentPredict(Resource):
    @api.response(200, "Success")
    @api.response(400, "Validation Error")
    @api.response(500, "Internal Error")
    @api.expect([req_item_predict])  # documents input field
    def post(self):
        """
        Make prediction for a single profile
        :return:
        """
        data = request.get_json(force=True)

        print(f'Processing data: "{data}"')
        resp = predict(data)
        logger.info(resp)

        # resp.update({"status": "Success"})
        return resp, 200
