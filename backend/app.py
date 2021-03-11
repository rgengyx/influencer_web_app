# Python Packages

# 3rd Party Packages
from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin

# Self-defined Packages and Modules
from api.VideoAPI import video_api
from api.MouseEventAPI import mouseEvent_api
from api.UserAPI import user_api
from api.ProductAPI import product_api

app = Flask(__name__)

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def render_index():
    return render_template('index.html')

@app.route("/description")
def render_description():
    return render_template('description.html')

@app.route("/instruction")
def render_instruction():
    return render_template('instruction.html')

@app.route("/product")
def render_product():
    return render_template('product.html')

@app.route("/thankyou")
def render_thankyou():
    return render_template('thankyou.html')

# API endpoints
app.register_blueprint(video_api, url_prefix='/api')
app.register_blueprint(mouseEvent_api, url_prefix='/api')
app.register_blueprint(user_api, url_prefix='/api')
app.register_blueprint(product_api, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=9808, debug=True)
