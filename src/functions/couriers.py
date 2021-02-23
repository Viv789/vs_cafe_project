import os
import csv
from tabulate import tabulate
from src.functions import menus
from src.functions.persistence import load_state, save_courier
from src.db.core import connection, courier_table

conn = connection()
state = load_state()

# Call and view the courier from the DB
def view_couriers(): 
    with conn.cursor() as cursor:
        sql_query = "SELECT * FROM courier"        
        cursor.execute(sql_query)
        result = cursor.fetchall()
    print(tabulate(result, headers=['ID', 'Name', 'Phone'], tablefmt='psql'))
        

#view courier from csv file
def courier_list(state):
    os.system("clear")
    print("ID Courier Name")
    print("--------------------")
    for row in state['couriers']:
        print(row['courier_id'] , row['courier_name'])

def new_courier(state):
    courier = state['couriers']
    courier_id = len(courier) +1
    courier_name = input('New courier name: ')
    courier_phone = int(input('courier phone: '))
    
    new_courier = {
        'courier_id':courier_id,
        'courier_name': courier_name, 
        'phone': courier_phone
        } 

    courier.append(new_courier)
    save_courier(courier) 
    print(new_courier)

    # save into db
    with conn.cursor() as cursor:
        sql_query = "INSERT INTO `courier`(`id`, `courier_name`,`phone`) VALUES (%s, %s, %s)"
        cursor.execute(sql_query,(courier_id, courier_name, courier_phone))
    conn.commit()

#update courier details
def update_courier(state):
    courier_list(state)
    courier = state['couriers']
    courier_id = int(input('Select Courier ID to update or 0 to cancel: ')) 
    if courier_id == 0:
        print('cancelling...')
        time.sleep(0.5)
        return courier
        
    elif courier_id != 0:
        courier_name = str(input('new courier name: '))
        if courier_name != '':
            courier[courier_id-1]['courier_name'] = courier_name
        courier_phone = str(input('new courier phone: '))
        if courier_phone != '':
            courier[courier_id-1]['phone'] = courier_phone
    
        update_courier = {
            'courier_id': courier_id,
            'courier_name': courier_name, 
            'phone': courier_phone
        }
            
        update_courier = {
            'courier_id': courier_id,
            'courier_name': courier_name, 
            'phone': courier_phone
        }
        
    save_courier(courier) 
    print(update_courier)

    #save to DB
    with conn.cursor() as cursor:
        sql_query = "UPDATE `courier`SET `courier_name` = %s,`phone` =  %s WHERE `id` = %s"
        cursor.execute(sql_query, (courier_name, courier_phone,courier_id))
    conn.commit()

#delete a courier
def delete_courier(state):
    courier_list(state)
    courier = state['couriers']
    idx = int(input('Select courier id to delete or 0 to cancel: '))
    if idx == 0:
        print('cancelling...')
        time.sleep(0.5)
        return courier
    if idx != 0:
        courier_index = int(idx) - 1
        del courier[courier_index]
        print(f'courier {idx} has been deleted')
    
    save_courier(courier) 
    
    #Save to DB
    with conn.cursor() as cursor:
        sql_query = "DELETE FROM `courier` WHERE(`id`) = (%s)"
        cursor.execute(sql_query, (idx))
    conn.commit()
