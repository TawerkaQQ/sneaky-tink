import os

import requests
from tinkoff.invest import Client, services, schemas
from tinkoff.invest.schemas import PortfolioRequest, PortfolioResponse

token = 't.wiOBWDjwSg9c9MQQeG5DSWu8NWn3BzvKHn91DzrTrbw_rFNOStU_6wKAZV4MRMed_r3XnvT4cPidUfxEIvnK9g'


class user_info:
    def __init__(self, token):
        self.token = token
        self.id = None

    def get_acc_info(self):
        with Client(self.token) as client:
            accounts = client.users.get_accounts()
            self.id = accounts.accounts[0].id
        return accounts


    def get_user_info(self):
        with Client(self.token) as client:
            user_info = client.users.get_info()
        return user_info

    def get_margin_info(self):
        with Client(self.token) as client:
            margin = client.users.get_margin_attributes(self.id)
        return margin

    def get_portfolio(self):

        portfolio = services.OperationsService.get_portfolio(self.id)
        print(portfolio)

        return portfolio



if __name__ == "__main__":
    user = user_info(token)
    acc = user.get_acc_info()
    print(acc)
    user_info = user.get_user_info()
    print(user_info)
    portfolio = user.get_portfolio()
    print(portfolio)

