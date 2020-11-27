from mysqldb import conn


def load_video():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM videos"
        cursor.execute(sql)
        result = cursor.fetchall()

    return result
