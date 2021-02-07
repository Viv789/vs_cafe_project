import os
from src.orders.core_order import new_order
from unittest.mock import patch
from unittest.mock import Mock

@patch('builtins.input')
@patch('builtins.print')
def test_new_order(mock_input, mock_print):
    mock_input.return_value = 'Jane','1 Test road', '074 456 7417','Hermes'
    new_order()
    mock_print.assert_called_with('Enter courier from list above: ')
    new_order()
    
test_new_order()       



