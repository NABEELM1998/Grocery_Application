import mysql.connector
__con =None
def get_Sql_connection():
    global __con
    if __con is None:
        __con = mysql.connector.connect(user='root', password='Nabeelm@86',
                                        host='localhost',
                                        database='grocery_store')
    return __con
    
    