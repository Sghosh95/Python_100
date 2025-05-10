import mysql.connector

# MySQL Connection to qa1_test
def get_user():
    try:
        mysql_qa1_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            port=3306,
            database='qa1_test'
        )
        if not mysql_qa1_connection.is_connected():
            raise Exception("Failed to connect to qa1_test database.")

        cursor = mysql_qa1_connection.cursor()
        cursor.execute("SELECT * FROM customer")
        result = cursor.fetchall()
        cursor.close()
        mysql_qa1_connection.close()
        return result

    except mysql.connector.Error as err:
        raise err
