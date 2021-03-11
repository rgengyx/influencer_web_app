import json
from flask import Blueprint
from service import ProductService
from flask import request

product_api = Blueprint('product_api', __name__)

@product_api.route('/product', methods=['GET'])
def get_product_by_id():
    productId = request.args.get('id')
    return json.dumps(ProductService.get_product_by_id(productId))


@product_api.route('/product/store_rating', methods=['POST'])
def store_rating():
    rating_dict = request.form.to_dict(flat=False)
    print(request.form)
    try:
        ProductService.store_rating(rating_dict)
        return "success"
    except KeyError:
        return "failure"

@product_api.route("/product/get_order", methods=['GET'])
def get_order():
    combo = request.args.get('combo')
    return json.dumps(ProductService.get_order(combo))