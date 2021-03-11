from mysqldb import conn
from pymysql.cursors import DictCursor

def get_product_by_id(productId):
    with conn.cursor(DictCursor) as cursor:
        sql = "SELECT * \
                FROM product \
                INNER JOIN review \
                ON product.id = review.productId \
                WHERE product.id = '{}'".format(productId)

        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def store_rating(rating_dict):
    with conn.cursor() as cursor:
        sql = "INSERT INTO rating VALUES ('" + rating_dict['userId'] + "','r1','" + rating_dict['r1'] + "','" + rating_dict['productId'] + "'),\
                ('" + rating_dict['userId'] + "','r2','" + rating_dict['r2'] + "','" + rating_dict['productId'] + "'),\
                ('" + rating_dict['userId'] + "','r3','" + rating_dict['r3'] + "','" + rating_dict['productId'] + "'),\
                ('" + rating_dict['userId'] + "','r4','" + rating_dict['r4'] + "','" + rating_dict['productId'] + "'),\
                ('" + rating_dict['userId'] + "','r5','" + rating_dict['r5'] + "','" + rating_dict['productId'] + "'),\
                ('" + rating_dict['userId'] + "','r6','" + rating_dict['r6'] + "','" + rating_dict['productId'] + "')"

        print(sql)
        cursor.execute(sql)
        conn.commit()

def get_order(combo):

    latin_product_review = None
    latin_product = None
    latin_review_combo = None

    with conn.cursor(DictCursor) as cursor:
        sql = "SELECT p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 \
                FROM latin_product_review \
                INNER JOIN latin_product_map \
                ON latin_product_review.review_order = latin_product_map.review_order \
                WHERE id = '{}'".format(combo)

        cursor.execute(sql)
        latin_product_review = cursor.fetchall()

    with conn.cursor(DictCursor) as cursor:
        sql = "SELECT product1, product2, product3, product4, product5, product6, product7, product8, product9, product10 \
                FROM latin_product_review \
                INNER JOIN latin_product \
                ON latin_product_review.product_order = latin_product.combo \
                WHERE id = '{}'".format(combo)

        cursor.execute(sql)
        latin_product = cursor.fetchall()

    with conn.cursor(DictCursor) as cursor:
        sql = "SELECT review1, review2,review3,review4,review5,review6 \
                FROM latin_review"

        cursor.execute(sql)
        latin_review_combo = cursor.fetchall()

    # print(latin_product_review, latin_product, latin_review_combo)
    return latin_product_review[0], latin_product[0], latin_review_combo