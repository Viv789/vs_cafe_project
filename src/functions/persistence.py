import csv
from src.db.core import connection, product_table, courier_table, order_table

conn = connection()

#function to view data in csv files
def read_csv_file(filename):
    data = []
    with open(filename, mode='r') as file:
        dict_reader = csv.DictReader(file)    
        for row in dict_reader: 
            data.append(row)
    return data

#function to write data into csv files
def write_csv_file(data, filename):
    with open(filename, mode='w', newline='\n') as file:
        dict_writer = csv.DictWriter(file, fieldnames=data[0].keys())
        dict_writer.writeheader()
        for row in data: 
            dict_writer.writerow(row)

# State management to load data
def load_state():
    state = {}
    state['products'] = read_csv_file('./data/products.csv')
    state['couriers'] = read_csv_file('./data/couriers.csv')
    state['orders'] = read_csv_file('./data/orders.csv')
    return state

def load_state_db():
    state = {}
    state['products'] = product_table()
    state['couriers'] = courier_table()
    state['orders'] = order_table()
    return state

# Functions to save changes in data files
state = load_state()

def save_product(state):
    with open('./data/products.csv', 'r+', newline='\n') as file:
        fieldnames = ['product_id', 'product_name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in state:
            writer.writerow(row)

def save_courier(state):
    read_csv_file('./data/couriers.csv')
    with open('./data/couriers.csv', 'w+', newline='\n') as file:
        fieldnames = ['courier_id', 'courier_name', 'phone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in state:
            writer.writerow(row)

def save_order(state):
    with open('./data/orders.csv', 'r+', newline='\n') as file:
        fieldnames = ['id', 'customer_name', 'customer_address', 'phone', 'courier', 'status', 'items']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in state:
            writer.writerow(row)
            