from flask_restplus import reqparse

comment_predict_parser = reqparse.RequestParser()
comment_predict_parser.add_argument("comment", type=str, required=True, location="json")
