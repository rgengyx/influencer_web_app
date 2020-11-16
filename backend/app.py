# Python Packages
import json

# 3rd Party Packages
from flask import Flask
from flask_cors import CORS, cross_origin

from sqlalchemy import create_engine, MetaData, Table
from api.VideoAPI import video_api

app = Flask(__name__)

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Database Connection
CONN_STR = 'mysql+pymysql://influencer:123456@localhost/influencer'
engine = create_engine(CONN_STR)
metadata = MetaData()

# API endpoints
app.register_blueprint(video_api)


@app.route("/")
def home():
    videos = Table('videos', metadata, autoload=True, autoload_with=engine)
    sql = videos.select()
    conn = engine.connect()
    result = conn.execute(sql)
    urls = {row[0]: row[1] for row in result}

    return json.dumps(urls)


if __name__ == '__main__':
    app.run(port=9808)
