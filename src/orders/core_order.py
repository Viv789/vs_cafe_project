import os
import csv
from src import app
from src.app_menus import update_order_menu
from src.couriers import core_courier

def view_orders():
    with open('orders.csv','r') as f:
        dict_reader = csv.DictReader(f)    
        for orders in dict_reader: 
            print(orders)


def new_order():
    name = input('Customer name: ')
    address = input('Customer address: ')
    phone = input('Customer phone number: ')
    print('order status: preparing')
    new_order = (f'{name},{address},{phone},{select_courier},preparing')
    with open('orders.csv','r+') as f: 
        for orders in f: 
            f.write(new_order)
            f.write('\n')
            print(f'New order: {new_order}')

order_status = ['processing','preparing','shipping','delivered']
