import requests


def _get_balance_api_url(account_id):
    """
    Get Balance URL for Monzo API
    """
    return 'https://api.getmondo.co.uk/balance?account_id={}'.format(
        account_id)


def _get_current_balance(account_id, access_token):
    """
    Get current account balance in pence from Monzo
    """
    response = requests.get(
        _get_balance_api_url(account_id),
        headers={'Authorization': 'Bearer {}'.format(access_token)})
    return response.json()['balance']
