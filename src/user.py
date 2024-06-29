import os
import requests
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tinkoff.invest import Client, services, schemas
from tinkoff.invest.schemas import PortfolioRequest, PortfolioResponse
from tinkoff.invest.services import OperationsService
from settings.settings import TOKEN, PORTFOLIO_NAME


class User:
    def __init__(self):
        pass

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

        with Client(TOKEN) as client:
            accounts = client.users.get_accounts().accounts
            for account in accounts:
                if account.name == PORTFOLIO_NAME:
                    print(account.id)
                    print(type(account))
                    return account
        '''
        Ввел параметр PORTFOLIO_NAME, так как у меня например 3 портфеля: личный, инвесткопилка, стратегия.
        Нужно решить что с этим делать, нужен ли параметр, так как работа планируется только с одним портфелем, но 
        все равно нужно где-то держать название портфеля.
        '''
        return None

    def get_user_info(self):

        """
        :return:
        (prem_status=False,
        qual_status=False,
        qualified_for_work_with=['russian_shares'],
        tariff='investor')
        """

        with Client(TOKEN) as client:
            user_info = client.users.get_info()
            print(user_info)
            '''
            Не знаю понадобится ли этот метод, насколько это нужная инфа? -> на обсуждение
            '''
        return user_info

    def get_margin_info(self):

        """
        :return:
        Маржинальность портфеля, у меня такой функции нет в портфеле, но она работает.
        А мне кажется нам это не нужно - не буду проверять.
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
        account = self.get_acc_info()
        with Client(TOKEN) as client:
            #operations_service = OperationsService(channel, metadata)
            #portfolio = operations_service.get_portfolio(account_id=self.id)
            portfolio = client.operations.get_portfolio(account_id=account.id)
            print(type(portfolio))
            print(portfolio.total_amount_shares)
        '''
        Не трогаю твой код. Мне кажется, то что я нашел больше подходит к портфелю. Посмотри объект 
        schemas.PortfolioResponse и его аттрибуты и уточни что конкретно ты нашел.
        '''
        return portfolio


if __name__ == "__main__":
    user = User()
    user.get_portfolio()

