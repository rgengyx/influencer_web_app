from dao import ProductDao

def get_product_by_id(productId):
    return ProductDao.get_product_by_id(productId)


def store_rating(rating_dict):
    for k, v in rating_dict.items():
        rating_dict[k] = v[0]
    # print(rating_dict)
    ProductDao.store_rating(rating_dict)