import os
from tabulate import tabulate
from src.db.core import connection
from src.functions.persistence import load_state
from src.functions import menus, products, couriers, orders

conn = connection()
state = load_state()

def enter():
    input("\nPress enter to continue")
    os.system("clear")

#Run through of main app
print('Welcome to SpecialTea Café')
print('------------------------------')
enter()

def start_app():
    
    print(f"\nMain Menu: {menus.main_menu}")
    
    while True :
        user_input = int(input("Enter option here: "))
        os.system("clear")
        
        if user_input == 0:
            print("Exited SpecialTea Café \nGoodbye!")
            exit()
        
        elif user_input == 1:
            while True:
                    print(menus.product_menu)
                    option_1 = int(input("Enter option: "))
                    os.system("clear")
                    if option_1 == 0:
                        start_app()
                    if option_1 == 1:
                        products.view_products()
                        enter()
                    if option_1 == 2:
                        products.new_product(state) 
                        enter()
                    if option_1 == 3:
                        products.update_product(state)
                        enter()
                    if option_1 == 4:
                        products.delete_product(state)
                        enter()
                    else:
                        print('Invalid option. Enter 0-4')
                    start_app()

        elif user_input == 2:
            while True:
                print(menus.courier_menu)
                option_2 = int(input("Enter option here: "))
                os.system("clear")
                if option_2 == 0:
                    start_app()
                if option_2 == 1:
                    couriers.view_couriers()
                    enter()
                if option_2 == 2:
                    couriers.new_courier(state)
                    enter()
                if option_2 == 3:
                    couriers.update_courier(state)
                    enter()
                if option_2 == 4:
                    couriers.delete_courier(state)
                    enter()
                else:
                    print('Invalid option. Enter 0-4')
                    start_app()

        elif user_input == 3:
            while True:
                print(menus.order_menu)
                option_3 = int(input("Enter option here: "))
                os.system("clear")
                if option_3 == 0:
                    start_app()
                if option_3 == 1:
                    orders.view_orders()
                    enter()
                if option_3 == 2:
                    orders.new_order(state)
                    enter()
                if option_3 == 3:
                    orders.update_order_status()
                    enter()
                else:
                    print('Invalid option. Enter 0-3')
                    start_app()
        break

start_app()