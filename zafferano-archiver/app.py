from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Version(Resource):
    def get(self):
        return {'app': 'zafferano-archiver', 'version': '0.1'}

api.add_resource(Version, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
