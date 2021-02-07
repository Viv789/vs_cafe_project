import os
import csv

def view_products() :
    with open('products.csv','r+') as f:
        idx = 0    
        print(f'\nProduct List: \n')
        dict_reader = csv.DictReader(f)
        for products in dict_reader: 
            print(f'{[idx]} , {products}')
            idx +=1
                
def new_product():
    product_name = str(input('product name: '))
    product_price = float(input('product price: '))
    new_product = (f'{product_name} ,{product_price}')
    with open('products.csv','r+') as f:
        dict_reader = csv.DictReader(f)
        for new_products in dict_reader:
            f.write(new_product)
            f.write('\n')
            print(new_product)

