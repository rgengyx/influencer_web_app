from mysqldb import conn
import uuid

def store_userInfo(userData_dict):
    with conn.cursor() as cursor:
        sql = "INSERT INTO user (id, age, gender, use_amazon, read_review) VALUES ('{}','{}','{}','{}','{}')".format(
                userData_dict['id'],
                userData_dict['age'],
                userData_dict['gender'],
                userData_dict['use_amazon'],
                userData_dict['read_review']
            )

        print(sql)
        cursor.execute(sql)
        conn.commit()

def store_agreement(agreementData_dict):
    with conn.cursor() as cursor:
        sql = "Update user SET agreement = 'Y' WHERE id = '{}'".format(
                agreementData_dict['id']
            )

        print(sql)
        cursor.execute(sql)
        conn.commit()
