import os
from src.functions.orders import list_orders, new_order
from unittest.mock import patch
from unittest.mock import Mock

@patch('builtins.input')
def test_new_order(mock_input):
    mock_input.return_value = 'Jane','1 Test road', '074 456 7417','Hermes'
    
# @patch('builtins.print')
# def test_view_orders():
    # new_order()
    # mock_print.assert_called_with('Customer name: ')
