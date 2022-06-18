from algosdk import account, mnemonic
from algosdk.constants import microalgos_to_algos_ratio
from algosdk.v2client import algod

def algod_client():
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = "JCOdQ28tND45xE5hobIx8OaNYYElRFR8XUVZQzH2"
    headers = {
        "X-API-Key": algod_token,
    }

    return algod.AlgodClient(algod_token, algod_address, headers)

def create_account():
    private_key, address = account.generate_account()
    return mnemonic.from_private_key(private_key)

def get_balance(address):
    account_info = algod_client().account_info(address)
    balance = account_info.get('amount') / microalgos_to_algos_ratio

    return balance