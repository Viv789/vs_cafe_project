import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
PASSWORD = os.environ.get("PASSWORD")
USER = os.environ.get("USER")
DB = os.environ.get("DB")


def connection():
    return pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DB)

conn = connection()

def product_table():
    with conn.cursor() as cursor:
        sql_query = "SELECT * FROM product"
        cursor.execute(sql_query)
        result = cursor.fetchall()
        #final_result = [list(i) for i in result]
        #print(final_result)
        for row in result:
            print(row)

def save_to_product():
    with conn.cursor() as cursor:
        sql_query = "INSERT INTO `product`(`id`,`name`,`price`) VALUES (%s, %s)"
        cursor.execute(sql_query, (product_id, product_name, product_price))
    #conn.commit()
    
def update_to_product():
    with conn.cursor() as cursor:
        sql_query = "UPDATE `product`(`name`,`price`) VALUES (%s, %s)"
        cursor.execute(sql_query, (product_name, product_price))
    #conn.commit()
    
def delete_to_product():
    with conn.cursor() as cursor:
        sql_query = "DELETE FROM `product` WHERE(`name`,`price`) = (%s, %s)"
        cursor.execute(sql_query, (product_name, product_price))
    #conn.commit()

def courier_table():
    with conn.cursor() as cursor:
        sql_query = "SELECT * FROM courier"
        cursor.execute(sql_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

def save_to_courier():
    with conn.cursor() as cursor:
        sql_query = "INSERT INTO `courier`(`name`,`phone`) VALUES (%s, %s)"
        cursor.execute(sql_query, (name,phone))
    #conn.commit()
    
def update_to_courier():
    with conn.cursor() as cursor:
        sql_query = "UPDATE `courier`(`name`,`phone`) VALUES (%s, %s)"
        cursor.execute(sql_query, (name, phone))
    #conn.commit()
    
def delete_to_courier():
    with conn.cursor() as cursor:
        sql_query = "DELETE FROM `courier` WHERE(`name`,`phone`) = (%s, %s)"
        cursor.execute(sql_query, (name, phone))
    #conn.commit()

def order_table():
    with conn.cursor() as cursor:
        sql_query = "SELECT * FROM transaction"
        cursor.execute(sql_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

def save_to_order():
    with conn.cursor() as cursor:
        sql_query = "INSERT INTO `transaction`(`name`,`address`,`phone`,`courier`,`status`,`items`) VALUES (%s, %s, %s, %s,%s, %s)"
        cursor.execute(sql_query, (name, address, phone,order_courier, "preparing", order_list))
    #conn.commit()
    
def update_to_courier_status():
    with conn.cursor() as cursor:
        sql_query = "UPDATE `courier`(`status`) VALUES (%s)"
        cursor.execute(sql_query, (row[idx]))
    #conn.commit()


# connection()
#product_table()
# courier_table()
#save_to_product() #check again
# delete_to_product()
# delete_to_courier()
# save_to_courier()
#order_table()
#update_to_courier_status()

import uuid

#print(uuid.uuid4())