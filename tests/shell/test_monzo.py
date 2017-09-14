import os
import responses

from moola.shell_monzo import _get_balance_api_url, _get_current_balance


@responses.activate
def test_get_current_balance():
    url = _get_balance_api_url(os.environ.get('MONZO_ACCOUNT_ID'))
    responses.add(responses.GET, url, json={'balance': 26822})

    balance = _get_current_balance(
        account_id=os.environ.get('MONZO_ACCOUNT_ID'),
        access_token=os.environ.get('MONZO_ACCESS_TOKEN'))

    assert balance == 26822
