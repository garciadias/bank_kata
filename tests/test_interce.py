import io
from contextlib import redirect_stdout
from datetime import datetime

import pytest

from bank_kata.domain.accounts import HEADER_STATEMENT, Account, AccountService


@pytest.fixture
def account():
    yield Account()


@pytest.fixture
def account_service():
    yield AccountService()


@pytest.fixture
def deposit_amount():
    yield 1000


@pytest.fixture
def account_with_one_deposit(account, account_service, deposit_amount):
    account_service.deposit(account, deposit_amount)
    yield account


@pytest.fixture
def header_statement():
    yield HEADER_STATEMENT


@pytest.fixture
def expected_statement_for_one_deposit(header_statement, deposit_amount):
    today = datetime.today().strftime("%d-%m-%Y")
    expected_statement = f"{header_statement}\n{today} || {deposit_amount:0.0f}   || {deposit_amount:0.0f}"
    yield expected_statement


def test_account_amount(account):
    assert account.balance == 0


def test_make_deposit(account_with_one_deposit):
    assert account_with_one_deposit.balance == 1000


def test_make_withdraw(account_with_one_deposit, account_service):
    account_service.withdraw(account_with_one_deposit, 500)
    assert account_with_one_deposit.balance == 500


def test_statement_for_empty_account(account, header_statement):
    assert isinstance(account.statement, str)
    assert account.statement == header_statement


def test_statement_has_statement_with_correct_deposit(
    account_with_one_deposit, expected_statement_for_one_deposit
):
    assert account_with_one_deposit.statement == expected_statement_for_one_deposit


def test_print_statement(
    account_with_one_deposit, account_service, expected_statement_for_one_deposit
):
    print("\n")
    account_service.statement(  # print statement on terminal for visual check
        account_with_one_deposit
    )
    f = io.StringIO()
    with redirect_stdout(f):
        account_service.statement(  # print statement on terminal and capture it
            account_with_one_deposit
        )
    s = f.getvalue()[:-1]
    assert s == expected_statement_for_one_deposit
