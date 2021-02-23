import os
import csv
import time
from tabulate import tabulate
from src.functions.products import product_list
from src.functions.couriers import courier_list
from src.functions.persistence import load_state, save_order
from src.db.core import connection

conn = connection()
state = load_state()

# View all orders
def view_orders():
    with conn.cursor() as cursor:
        sql_query = "SELECT * FROM transaction"        
        cursor.execute(sql_query)
        result = cursor.fetchall()
    print(tabulate(result, headers=['ID', 'Name', 'Address', 'Phone', 'Courier', 'Status', 'Items'], tablefmt='psql'))
    
def list_orders(state): 
    print('ID Customer Name')
    print('------------------')
    for row in state['orders']:
        print(row['id'],row['customer_name'])

# Create a new order, select products and assign a courier
def new_order(state):
    orders = state['orders']
    
    name = input('Customer name: ')
    address = input('Customer address: ')
    phone = (input('Customer phone number: '))
    
    #screen sleeps for a period of time before moving on
    time.sleep(0.5)
    os.system('clear')
    
    order_list = []
    product_list(state)
    print('select product id to purchase or 0 to cancel: ')
    while True:
        purchase = int(input())
        if purchase != 0:
            print('enter another item id or 0 to end: ')
        if purchase == 0:
            print('purchase completed')
            break
        order_list.append(purchase)
        
    #let user know they should pick a courier
    time.sleep(0.5)
    courier_list(state) 
    dispatcher = int(input('select courier id from the list: '))
    
    print('order status: preparing......')
    time.sleep(1)
    os.system("clear")
    
    new_order = {
        'id':len(orders) +1,
        'customer_name': name,
        'customer_address': address,
        'phone': phone,
        'courier': dispatcher, 
        'status': 'preparing',
        'items': order_list 
        } 
    
    print(new_order)
    orders.append(new_order)
    save_order(orders)
    #Insert into DB
    with conn.cursor() as cursor:
        sql_query = "INSERT INTO `transaction`(`name`,`address`,`phone`,`courier`,`status`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql_query,(name, address, phone, dispatcher, 'preparing'))
    conn.commit()

def order_status():
    order_status= ['preparing','shipping','delivered']
    print('ID Order Staus')
    print('---------------')
    for i in enumerate(order_status, start=1):
        print(i)

#Update the status of orders from the default
def update_order_status():
    list_orders(state)
    idx = (int(input('select order ID to update status: ')) -1)
    index = int(idx)+1
    with open('./data/orders.csv','r+') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
        order_state= ['preparing','shipping','delivered']
        order_status()
        select_order_status = int(input('Select ID of updated order status: ')) -1
    with open('./data/orders.csv','w+', newline='\n') as file:
        rows[idx][5] = order_state[select_order_status]
        status = rows[idx][5] 
        writer = csv.writer(file) 
        writer.writerow(header)
        writer.writerows(rows)
    print(rows[idx]) 
    
    with conn.cursor() as cursor:
        sql_query = "UPDATE `transaction` SET `status` = %s  WHERE `id` = %s"
        cursor.execute(sql_query, (status, index))
    conn.commit()