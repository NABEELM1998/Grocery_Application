from sql_connection import get_Sql_connection
def get_All_Products(connection):
    cur = connection.cursor()
    query = "select p.product_id, p.Name, p.uom_id, p.price_per_unit,u.uom_name from products p"
    query = query + " join uom u on p.uom_id = u.uom_id;"
    cur.execute(query)
    response = []
    for (product_id, Name, uom_id, price_per_unit, uom_name) in cur:
        response.append(
            {
                "product_id": product_id,
                "Name" : Name,
                "uom_id" : uom_id,
                "price_per_unit" : price_per_unit,
                "uom_name" : uom_name
            }
        )
    connection.close()
    return response

def insert_Product(connection,products):
    cnx = connection.cursor()
    add_products = ("INSERT INTO products "
               "( Name, uom_id, price_per_unit) "
               "VALUES ( %s, %s, %s)")
    data = (products['Name'],products['uom_id'],products['price_per_unit'])

    cnx.execute(add_products,data)
    connection.commit()
    connection.close()
    return cnx.lastrowid
def delete_Products(connection,product_id):
    cnx = connection.cursor()
    query = "DELETE from products where product_id = " + str(product_id)
    cnx.execute(query)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    connection = get_Sql_connection()  
    #print(get_All_Products(connection))
    #print(insert_Product(connection,{"Name":'Sugar',"uom_id":2,"price_per_unit":50}))
    delete_Products(connection,4)