import os
from src.couriers.core_courier import new_courier
from unittest.mock import Mock
from unittest.mock import patch

@patch('builtins.input')
def test_new_courier(mock_input):
    mock_input.return_value = 'Alex, 07892580041'
    new_courier()
    mock_input.call_count

test_new_courier()





# mock_new_courier = Mock()
# mock_new_courier.return_value = 'Amazon'
# mock_new_courier()
# mock_new_courier.call_count
# print(mock_new_courier())
# print(mock_new_courier.call_count)
# print(mock_new_courier.assert_called())
# mock_new_courier.reset_mock()
# mock_new_courier.assert_called()

