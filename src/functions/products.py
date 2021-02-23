import os
import csv
import time
from tabulate import tabulate
from src.functions.persistence import load_state, save_product
from src.functions import menus
from src.db.core import connection

# This sets the connection to the database
conn = connection()
state = load_state()

# View current product stock with prices
def view_products(): 
    with conn.cursor() as cursor:
        sql_query = "SELECT * FROM product"        
        cursor.execute(sql_query)
        result = cursor.fetchall()
    print(tabulate(result, headers=['ID', 'Name', 'Price'], tablefmt='psql'))
        
# Product list         
def product_list(state):
    os.system('clear')
    print('ID Product Name')
    print('------------------')
    for row in state['products']:
        print(row['product_id'] , row['product_name'])

# Create a new product
def new_product(state):
    product = state['products']
    print('Create new product: ') 
    product_id = len(product) +1
    product_name = str(input('product name: '))
    product_price = float(input('enter product price: '))
    
    new_product = {
        'product_id':product_id, 
        'product_name':product_name, 
        'price':product_price
        }
    
    product.append(new_product)
    save_product(product) 
    
    # connect to DB
    with conn.cursor() as cursor:
        sql_query = "INSERT INTO `product`(`id`,`name`,`price`) VALUES (%s, %s, %s)"
        cursor.execute(sql_query, (product_id, product_name, product_price))
    conn.commit()


# update current product stock
def update_product(state):
    product_list(state)
    product = state['products']
    product_id = int(input('Select product ID to update or 0 to cancel: ')) 
    
    if product_id == 0:
        print('cancelling...')
        time.sleep(0.5)
        return product

    elif product_id != 0:
        product_name = str(input('new product name: '))
        if product_name != '':
            product[product_id-1]['product_name'] = product_name
        
        product_price = input('new product price: ')
        if product_price != '':
            product[product_id-1]['price'] = float(product_price)
            
        update_product = {
            
        'product_id':product_id, 
        'name':product_name, 
        'price':product_price
        }

        save_product(product)
        print(update_product)
    
    #this is to commit to DB 
    with conn.cursor() as cursor:
        sql_query = "UPDATE `product`SET `name` = %s,`price` =  %s WHERE `id` = %s"
        cursor.execute(sql_query, (product_name, product_price,product_id))
    conn.commit()

# Delete a product that is no longer on offer
def delete_product(state):
    product_list(state)
    product = state['products']
    idx = int(input('Please select ID of the product to delete or 0 to cancel: '))
    if idx == 0 :
        print('cancelling...')
        time.sleep(0.5)
        return product
    if idx != 0:
        product_index = int(idx)- 1
        del product[product_index] 
        print(f'product:{idx} has been deleted')
        
    save_product(product)

        #this is link to db
    with conn.cursor() as cursor:
        sql_query = "DELETE FROM `product` WHERE(`id`) = (%s)"
        cursor.execute(sql_query, (index))
    conn.commit()
