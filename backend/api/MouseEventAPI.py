from flask import Blueprint
from flask import request
from service import MouseEventService

mouseEvent_api = Blueprint('mouseEvent_api', __name__)


@mouseEvent_api.route('/mouseEvent', methods=['POST'])
def update_mouseEvent():
    data = request.get_json()
    MouseEventService.store(data)
    return "post request"
