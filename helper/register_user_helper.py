from test import connection


def user_register(user_id, mobile_no, email, name, gender, is_available, is_deleted):
    cursor = connection.cursor()
    query = "INSERT INTO users(user_id,mobile_no,email,name,gender,is_available,is_deleted) VALUES(%s,%s,%s," \
            "%s,%s,%s,%s) "
    v = (user_id, mobile_no, email, name, gender, is_available, is_deleted)
    s = cursor.execute(query, v)
    connection.commit()
    cursor.close()


def update_data(mobile_no, email):
    cursor = connection.cursor()
    query1 = "UPDATE users SET mobile_no =%s WHERE email =%s "
    v = (mobile_no, email)
    r = cursor.execute(query1, v)
    connection.commit()
    cursor.close()
