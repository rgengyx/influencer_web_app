# Python Packages
import json
from flask import Blueprint
from service import UserService
from flask import request

user_api = Blueprint('user_api', __name__)


@user_api.route('/user', methods=['POST'])
def store_userInfo():
    #immutableMultidict
    userData_dict = request.form.to_dict(flat=False)
    print(userData_dict)
    UserService.store_userInfo(userData_dict)
    return "success"