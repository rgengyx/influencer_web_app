# Python Packages
import json
from flask import Blueprint
from service import UserService
from flask import request
from flask import jsonify
user_api = Blueprint('user_api', __name__)


@user_api.route('/user/store', methods=['POST'])
def store_userInfo():
    #immutableMultidict
    userData_dict = request.form.to_dict(flat=False)
    print("userData_dict", userData_dict)
    try:
        UserService.store_userInfo(userData_dict)
        return "success"
    except KeyError:
        return "failure"

@user_api.route('/user/store_agreement', methods=['POST'])
def store_agreement():
    #immutableMultidict
    agreementData_dict = request.form.to_dict(flat=False)
    print(agreementData_dict)
    try:
        UserService.store_agreement(agreementData_dict)
        return "success"
    except KeyError:
        return "failure"