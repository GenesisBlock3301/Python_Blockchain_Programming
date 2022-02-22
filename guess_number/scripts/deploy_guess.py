import os
from dotenv import load_dotenv
from brownie import accounts,GuessNum,Wei

load_dotenv()

def main():
    deploy_account = accounts.add(os.environ["PRIVATE_KEY_1"])
    deploy_detail = {
        'from':deploy_account,
        'value':Wei('10 ether'),
    }
    guess_number = GuessNum.deploy(9,deploy_detail)
    return guess_number