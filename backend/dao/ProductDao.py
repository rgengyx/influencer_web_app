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
