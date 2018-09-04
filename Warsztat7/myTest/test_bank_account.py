from unittest.mock import patch
import random
import pytest

from bank_account import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount()

def test_zero_on_new_account(bank_account):
    bank_account = BankAccount()

    assert bank_account.get_balance() == 0

def test_balance_after_deposit(bank_account):
    bank_account.deposit(100)

    assert bank_account.get_balance() == 100

def test_balance_after_deposit_2(bank_account):
    bank_account.deposit(200)

    assert bank_account.get_balance() == 200

def test_balance_after_deposit_3(bank_account):
    bank_account.deposit(200)
    bank_account.deposit(100)

    assert bank_account.get_balance() == 300

def test_balance_after_deposit_with_promo(bank_account):
    with patch('random.random') as mock_obj:
        mock_obj.return_value = 0.05
        bank_account.deposit(100, with_promo = True)
    
    assert bank_account.get_balance() == 101

def test_balance_after_deposit_with_promo_2(bank_account):
    with patch('random.random') as mock_obj:
        mock_obj.return_value = 0.5
        bank_account.deposit(100, with_promo = True)
    
    assert bank_account.get_balance() == 100