# Python Packages
import json

from flask import Blueprint
from service import VideoService

video_api = Blueprint('video_api', __name__)


@video_api.route('/video', methods=['GET'])
def load_video():
    return VideoService.load_video()
