import os
from src.functions.couriers import new_courier, delete_courier
from unittest.mock import Mock
from unittest.mock import patch

@patch('builtins.print')
def view_couriers(mock_print): 
    view_couriers()
    mock_print.assert_called_with('tabulate(result, headers=[ID, Name, Phone], tablefmt=psql')

@patch('builtins.input')
@patch('builtins.print')
def test_new_courier(mock_input, mock_print):
    mock_input.return_value = 'courier phone: '
    mock_input.call_count
    # new_courier()
    # mock_print.assert_called_with('courier_id') 

@patch('builtins.input')
def test_delete_courier(mock_input):
    mock_input.return_value = 'Select courier to delete: '



# @patch('builtins.input')
# @patch('builtins.print')
# def test_new_courier(mock_input, test_courier):
    
#     mock_input.return_value = 'Alex, 07892580041'
#     test_courier = 'Alex, 07892580041'
#     mock_input.call_count

