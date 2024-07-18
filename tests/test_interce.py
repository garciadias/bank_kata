from bank_kata.domain.accounts import Account, AccountService


def test_print_statement_for_empty_account():
    account = Account()
    account_service = AccountService()
    assert isinstance(account_service.statement(account), str)
