from dao import ProductDao

def get_product_by_id(productId):
    return ProductDao.get_product_by_id(productId)


def store_rating(rating_dict):
    for k, v in rating_dict.items():
        rating_dict[k] = v[0]
    # print(rating_dict)
    ProductDao.store_rating(rating_dict)

def get_order(combo):
    product_review, product_order, review_order = ProductDao.get_order(combo)

    product_review_latin = []
    for k, v in product_order.items():
        review_combo = int(product_review[v])
        product_review_latin.append([v, list(review_order[review_combo - 1].values())])

    return product_review_latin