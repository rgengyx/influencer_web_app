# Python Packages

# 3rd Party Packages
from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin

# Self-defined Packages and Modules
from api.VideoAPI import video_api
from api.MouseEventAPI import mouseEvent_api
from api.UserAPI import user_api

app = Flask(__name__)

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return render_template('index.html')

# API endpoints
app.register_blueprint(video_api, url_prefix='/api')
app.register_blueprint(mouseEvent_api, url_prefix='/api')
app.register_blueprint(user_api, url_prefix='/api')


if __name__ == '__main__':
    app.run(port=9808, debug=True)
