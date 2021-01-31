main_menu = """
[0] To Exit app 
[1] For Product Menu 
[2] For Courier Menu 
[3] For Order Menu
"""

products = ["Apple", "Samsung", "Huawei", "Nokia"]
product_menu = """
[0] Return to Main Menu 
[1] View Products  
[2] Create new product
"""

couriers = ["DHL", "Hermes", "Royal Mail"]
courier_menu = """
[0] Return to Main Menu 
[1] View Couriers 
[2] Create new courier
"""
order_menu = """
[0] Return to Main Menu 
[1] View Orders 
[2] Create new order
[3] Update order status
"""

import os
import functions

# #Products list
with open('products.txt','r+') as f:    
        print(f'Product List: \n')
        for line in f: 
            line = line.strip()
            print(line)

#Couriers list
with open('couriers.txt','r+') as f:
        print('Courier List: \n')  
        for line in f:
            line = line.strip()            
            print(line)

def start_app():

    print(f"User options: {main_menu}")
    
    while True :
        user_input = int(input("Enter option here: "))
        os.system("clear")
        
        if user_input == 0:
            print("Exited app")
            exit()
            
        elif user_input == 1:
            while True:
                print(product_menu)
                option_1 = int(input("Enter option: "))
                os.system("clear")
                if option_1 == 0:
                    start_app()
                if option_1 == 1:
                    print(products)
                    input("press enter to continue")
                    os.system("clear")
                if option_1 == 2:
                    functions.new_product()

        elif user_input == 2:
            while True:
                print(courier_menu)
                option_2 = int(input("Enter option here: "))
                os.system("clear")
                if option_2 == 0:
                    start_app()
                if option_2 == 1:
                    print(couriers)
                    input("press enter to continue")
                    os.system("clear")
                if option_2 == 2:
                    functions.new_courier()

        elif user_input == 3:
            while True:
                print(order_menu)
                option_3 = int(input("Enter option here: "))
                os.system("clear")
                if option_3 == 0:
                    start_app()
                if option_3 == 1:
                    functions.view_orders()
                if option_3 == 2:
                    functions.new_order()
                if option_3 == 3:
                    functions.update_order()
        break

start_app()
