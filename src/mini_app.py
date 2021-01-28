products = ["Apple", "Samsung", "Huawei", "Nokia"]
courier = ["DHL", "Hermes", "Yodel", "Royal Mail"]
options = ("[0] To Exit app", "[1] For Product Menu", "[2] For Courier Menu")
product_menu = ("[0] Return to Main Menu ", "[1] View Products ", "[2] Create new product") 
courier_menu = ("[0] Return to Main Menu ", "[1] View Couriers ", "[2] Create new courier") 
    
import os

#Products list
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

    print("User options:")
    for i in range(len(options)):
        print(options[i])
        
    while True :
        user_input = int(input("Enter option : "))
        os.system("clear")
        
        if user_input == 0:
            print("exited app")
            exit()
            
        elif user_input == 1:
            while True:
                for i in range(len(product_menu)):
                    print(product_menu[i])
                choice = int(input("Enter option: "))
                
                os.system("clear")
                
                if choice == 0:
                    start_app()
                if choice == 1:
                    print(products)
                    input("press enter to continue")
                    os.system("clear")
                if choice == 2:
                    new_product = input("New product name : ")
                    products.append(new_product)
                    print(products)
                    with open("products.txt",'a') as f:
                        f.write(new_product)
                        f.write("\n")
                    input("press enter to continue")
                    os.system("clear")

        elif user_input == 2:
            while True:
                for i in range(len(courier_menu)):
                    print(courier_menu[i])
                selected = int(input("Enter choice here"))
                os.system("clear")
                if selected == 0:
                    start_app()
                if selected == 1:
                    print(courier)
                    input("press enter to continue")
                    os.system("clear")
                if selected == 2:
                    new_courier = input("New courier name : ")
                    courier.append(new_courier)
                    print(courier)
                    with open("couriers.txt",'a') as f:
                        f.write(new_courier)
                        f.write("\n")
                    input("press enter to continue")
                    os.system("clear")
        break

start_app()

