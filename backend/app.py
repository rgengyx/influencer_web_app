# Python Packages

# 3rd Party Packages
from flask import Flask
from flask_cors import CORS, cross_origin

# Self-defined Packages and Modules
from api.VideoAPI import video_api

app = Flask(__name__)

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# API endpoints
app.register_blueprint(video_api, url_prefix='/')

if __name__ == '__main__':
    app.run(port=9808)
