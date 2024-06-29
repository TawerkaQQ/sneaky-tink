import os
import requests

from tinkoff.invest import Client, services, schemas
from tinkoff.invest.schemas import PortfolioRequest, PortfolioResponse
from tinkoff.invest.services import OperationsService


class UserInfo:
    def __init__(self, token):
        self.token = token
        self.id = None

    def get_acc_info(self):

        """
        :return: (accounts=[Account(id='2061614988',
        type=<AccountType.ACCOUNT_TYPE_TINKOFF: 1>,
        name='Брокерский счет',
        status=<AccountStatus.ACCOUNT_STATUS_OPEN: 2>,
        opened_date=datetime.datetime(2023, 8, 6, 0, 0, tzinfo=datetime.timezone.utc),
        closed_date=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        access_level=<AccessLevel.ACCOUNT_ACCESS_LEVEL_FULL_ACCESS: 1>)])
        """

        with Client(self.token) as client:
            accounts = client.users.get_accounts()
            self.id = accounts.accounts[0].id
        return accounts

    def get_user_info(self):

        """
        :return:
        (prem_status=False,
        qual_status=False,
        qualified_for_work_with=['russian_shares'],
        tariff='investor')
        """

        with Client(self.token) as client:
            user_info = client.users.get_info()
        return user_info

    def get_margin_info(self):

        """
        :return:
        Маржинальность портфеля, у меня такой функции нет в портфеле, но она работает.
        """

        with Client(self.token) as client:
            margin = client.users.get_margin_attributes(self.id)
        return margin

    def get_portfolio(self):
        """
        :return:
        money - Массив валютных позиций портфеля.
        blocked - Массив заблокированных валютных позиций портфеля.
        securities - Список ценно-бумажных позиций портфеля.
        limits_loading_in_progress - Признак идущей в данный момент выгрузки лимитов.
        futures - Список фьючерсов портфеля.
        options - Список опционов портфеля.
        """

        with Client(self.token) as client:
            operations_service = OperationsService(channel, metadata)
            portfolio = operations_service.get_portfolio(account_id=self.id)
            print(portfolio)

        return portfolio


if __name__ == "__main__":
    token = ''
    user = UserInfo(token)
    acc = user.get_acc_info()
    print(acc)
    user_info = user.get_user_info()
    print(user_info)
    portfolio = user.get_portfolio()
    print(portfolio)
