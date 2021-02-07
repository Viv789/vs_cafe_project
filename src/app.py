import os
from src import app_menus
from src.products import core_product
from src.couriers import core_courier
from src.orders import core_order

def enter():
    input("\npress enter to continue")
    os.system("clear")

def start_app():
    
    print(f"\nUser options: {app_menus.main_menu}")
    
    while True :
        user_input = int(input("Enter option here: "))
        os.system("clear")
        
        if user_input == 0:
            print("Exited app \nGoodbye!")
            exit()
        
        elif user_input == 1:
            while True:
                    print(app_menus.product_menu)
                    option_1 = int(input("Enter option: "))
                    os.system("clear")
                    if option_1 == 0:
                        start_app()
                    elif option_1 == 1:
                        core_product.view_products()
                        enter()
                    elif option_1 == 2:
                        core_product.new_product() #fix up and check
                        enter()
                    start_app()

        elif user_input == 2:
            while True:
                print(app_menus.courier_menu)
                option_2 = int(input("Enter option here: "))
                os.system("clear")
                if option_2 == 0:
                    start_app()
                if option_2 == 1:
                    core_courier.couriers()
                    enter()
                if option_2 == 2:
                    core_courier.new_courier()
                    enter()

        elif user_input == 3:
            while True:
                print(app_menus.order_menu)
                option_3 = int(input("Enter option here: "))
                os.system("clear")
                if option_3 == 0:
                    start_app()
                if option_3 == 1:
                    core_order.view_orders()
                    enter()
                if option_3 == 2:
                    core_order.new_order()
                    enter()
                if option_3 == 3:
                    core_order.update_order_status()
        break

start_app()

