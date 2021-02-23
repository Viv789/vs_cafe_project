import os
from src.functions.products import delete_product
from unittest.mock import patch
from unittest.mock import Mock

# @patch('builtins.input')
# @patch('builtins.print')
# def test_new_product(mock_input, mock_print):
#     mock_input.return_value = 'product name: ', 'enter product price: '
#     #mock_print.assert_called_with('id: product_id, name:product_name,price:product_price')

# test_new_product()

# @patch('builtins.input')
# @patch('builtins.print')
# def test_delete_product(state,mock_input, mock_print):
#     test_state = state['products']
#     mock_input.return_value = 'Please select ID of the product to delete or 0 to cancel: ' 
#     mock_print.assert_called_with(f'product:{idx} has been deleted')
    
# test_delete_product(state)