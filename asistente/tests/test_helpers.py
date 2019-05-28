from unittest.mock import patch, MagicMock
from asistente.helpers import delete_subscription_from_stripe


@patch('asistente.helpers.stripe.Subscription.retrieve')
def test_delete_subscription(mock_function):
    """Tests the helper method that uses stripe for deleting subscriptions"""

    # Mocking the Subscription retrieve method to return a mock with a
    # mocked delete method
    subscription_mock = MagicMock()
    subscription_mock.delete = MagicMock()
    mock_function.return_value = subscription_mock

    # Calling the helper function
    delete_subscription_from_stripe('123456')

    # the retrieve and delete functions should be called
    mock_function.assert_called_once_with('123456')
    subscription_mock.delete.assert_called_once_with()

