# Function to feed into mini app

products = ["Apple", "Samsung", "Huawei", "Nokia"]
product_menu = ("[0] Return to Main Menu ", "[1] View Products ", "[2] Create new product") 
courier = ["DHL", "Hermes", "Royal Mail"]
courier_menu = ("[0] Return to Main Menu ", "[1] View Couriers ", "[2] Create new courier") 
update_menu = ("[0] To cancel ", "[1] To update order status ") 

import os
import csv

#def functions():
    
def new_product():
    new_product = input("New product name : ")
    products.append(new_product)
    print(products)
    with open("products.txt",'a') as f:
        f.write(new_product)
        f.write("\n")
    input("press enter to continue")
    os.system("clear")
    
def new_courier():
    new_courier = input("New courier name : ")
    courier.append(new_courier)
    print(courier)
    with open("couriers.txt",'a') as f:
        f.write(new_courier)
        f.write("\n")
    input("press enter to continue")
    os.system("clear")
    

def view_orders():
    with open('orders.csv','r') as f:
        dict_reader = csv.DictReader(f)    
        for orders in dict_reader: 
            print(orders)
    input("press enter to continue")
    os.system("clear")

def new_order():
    name = input('Customer name: ')
    address = input('Customer address: ')
    phone = input('Customer phone number: ')
    print(courier)
    select_courier = input('Enter courier from list above: ')
    print('order status: preparing')
    new_order = (f'{name},{address},{phone},{select_courier}, preparing')
    with open('orders.csv','r+') as f: 
        for orders in f: 
            f.write(new_order)
            f.write('\n')
            print(f'New order: {new_order}')
            input("press enter to continue")
            os.system("clear")








