from flask import Flask
from sqlalchemy import create_engine, MetaData, Table
from api.VideoAPI import video_api

app = Flask(__name__)

# Database Connection
CONN_STR = 'mysql://influencer:123456@localhost/influencer'
engine = create_engine(CONN_STR, echo=True)
metadata = MetaData()

# API endpoints
app.register_blueprint(video_api)


@app.route("/")
def home():
    videos = Table('videos', metadata, autoload=True, autoload_with=engine)
    sql = videos.select();
    conn = engine.connect()
    result = conn.execute(sql)
    return result


if __name__ == '__main__':
    app.run(port=5000)
