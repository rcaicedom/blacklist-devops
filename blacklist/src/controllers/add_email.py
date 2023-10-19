from flask_restful import Resource
from flask import request
from src.schema.email_schema import PostAddEmailSchema


class AddEmail(Resource):
    def post(self):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        email_add_schema = PostAddEmailSchema()
        errors = email_add_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        email_add_dump = email_add_schema.dump(request_json)

        email_add_dump["ip"] = request.remote_addr

        print(email_add_dump)
        
        return email_add_dump, 200