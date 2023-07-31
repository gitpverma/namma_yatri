from flask import request, jsonify
from flask_restful import Resource

from helper.register_user_helper import user_register, update_data


class Registration(Resource):
    def post(self):
        params = request.get_json()
        user_id = params.get('user_id')
        mobile_no = params.get('mobile_no')
        email = params.get('email')
        name = params.get('name')
        gender = params.get('gender')
        is_available = params.get('is_available')
        is_deleted = params.get('is_deleted')
        print(user_id)
        final_result = user_register(user_id, mobile_no, email, name, gender, is_available, is_deleted)
        data = {'user_id': user_id, 'mobile_no': mobile_no, 'email': email, 'name': name, 'gender': gender,
                'is_available': is_available, 'is_deleted': is_deleted}
        print(data)
        return jsonify(data=data, code=200)


class Update(Resource):
    def put(self):
        params = request.get_json()
        email = params.get('email')
        mobile_no = params.get('mobile_no')
        result = update_data(mobile_no, email)
        print(result)

        resp = {"message": "mobile_no updated successfully", "code": 200}
        return jsonify(data=resp, code=200)

