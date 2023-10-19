from flask import Flask
from flask_restful import Api
from src.controllers.add_email import AddEmail

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(AddEmail, '/blacklists')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000, host='0.0.0.0')
