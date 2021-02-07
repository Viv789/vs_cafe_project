import os
import csv

def couriers() :
    with open('couriers.csv','r+') as f:
            print('\nCourier List: \n')  
            dict_reader = csv.DictReader(f)
            for courier in dict_reader:           
                print(courier)

def new_courier(): 
    courier_name = input('New courier name: ')
    courier_phone = int(input('courier phone: '))
    new_courier = (f'{courier_name}, {courier_phone}')
    with open('couriers.csv','r+') as f:
        for courier in f:
            f.write(new_courier)
            f.write('\n')
            print(new_courier)

