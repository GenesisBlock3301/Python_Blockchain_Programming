import pytest
from brownie import Wei, accounts, GuessNum


@pytest.fixture
def guess_number():
    return GuessNum.deploy(7, {'from': accounts[0], 'value': Wei('10 ether')})


def test_play_wrong_guess(guess_number):
    pre_contract_balance = guess_number.getBalance()
    pre_player_balance = accounts[1].balance()
    guess_number.play(
        accounts[1], 6, {'from': accounts[1], 'value': Wei('1 ether')})

    assert accounts[1].balance() == pre_player_balance - Wei('1 ether') 
    assert guess_number.currState() == 0

def test_right_guess(guess_number):
    pre_contract_balance = guess_number.getBalance()
    pre_player_balance = accounts[1].balance()
    guess_number.play(
        accounts[1], 7, {'from': accounts[1], 'value': Wei('1 ether')})

    assert guess_number.getBalance() == 0
