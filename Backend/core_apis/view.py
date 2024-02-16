from flask import Flask, Blueprint, Response, request, jsonify, make_response
from flask_restx import Api, Resource, fields, reqparse
from core_apis.payloads import *




api = Api()


mango_ai = Blueprint('mango', __name__, url_prefix='/mango')
mango_api = Api(mango_ai, version="1.0", title="mango", description="Mango AI Virtual Assistant")
mangons = mango_api.namespace('mango', description='Mango AI Virtual Assistant')

nested_model = api.model('NestedModel', {
    'nested_field': fields.String(description='Nested Field'),
})
main_model = api.model('MainModel', {
    'field1':  fields.String(description='Field 1'),
    'nested': fields.Nested(nested_model),
})


@mangons.route('/server_test')
class ServerTest(Resource):
    @api.expect(server_test, validate=True)
    def get(self):
        try:
            args = server_test.parse_args()
            val = args['arg']
            print(val)
            return 'server running', 200
        except Exception as e:
            print('Error in My Route : ', e)



@mangons.route('talktome/friend')
class TTM_friend(Resource):
    @api.expect(ttm_friend, validate=True)
    def post(self):
        try:
            return 'server running', 200
        except Exception as e:
            print('Error in My Route : ', e)