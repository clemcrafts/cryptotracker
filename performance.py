import csv
from matplotlib import pyplot as plt


class Performance:
    """
    Class in charge of tracking the performance of a crypto portfolio against
    the entire crypto asset class.
    We use yahoo finance data format (file export) for assert prices
    """

    def __init__(self, portfolio):
        """
        Define assets held in portfolio and initialize data structure.
        :param dict portfolio: the portfolio to analyse.
        e.g: {'btc': 1.5, 'eth': 33} means that it holds 1.5 BTC and 33 ETH.
        """
        self.portfolio = portfolio
        self.asset_prices = {}
        for asset in self.portfolio.keys():
            self.asset_prices[asset] = []
        self.portfolio_prices = []
        self.portfolio_performance = []
        self.crypto_prices = []
        self.crypto_performance = []

    def load_prices(self):
        """
        Loading the data from yahoo finance data format.
        n.b: As an example, for Bitcoin you can go to:
        https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD
        And "download" the file that you can move to this directory.
        """
        for asset in self.portfolio.keys():
            self.load_crypto_prices(
                'data/{}.csv'.format(asset), self.asset_prices[asset])

    def load_crypto_market_cap(self, days_to_consider_from_today=10):
        """
        Loading total crypto market cap.
        n.b: entered manually, to be automated
        """
        with open('data/total.csv', 'r') as file:
            for line, row in enumerate(csv.reader(file)):
                if line == 0:
                    continue
                self.crypto_prices.append(float(row[1]))

    @staticmethod
    def load_crypto_prices(file, asset, days_to_consider_from_today=10):
        """
        Loading crypto prices.
        :param str file: the file to load from.
        :param str asset: the asset considered (e.g: btc)
        :param int days_to_consider_from_today: number of days to look at.
        """
        with open(file, 'r') as file:
            for line, row in enumerate(reversed(list(csv.reader(file)))):
                if line > days_to_consider_from_today-1:
                    continue
                if 'null' in row:
                    continue
                asset.append(float(row[4]))

    def get_porfolio_prices(self):
        """
        Getting the prices of the entire portfolio day by day.
        """
        for portfolio_asset_key in self.asset_prices.keys():
            for day, price in enumerate(
                    reversed(self.asset_prices[portfolio_asset_key])):
                quantity = self.portfolio[portfolio_asset_key]
                try:
                    self.portfolio_prices[day] += quantity * price
                except IndexError:
                    self.portfolio_prices.append(quantity * price)

    def get_porfolio_performance(self):
        """
        Getting the performance of the portfolio day by day.
        """
        initial_price = self.portfolio_prices[0]
        for porfolio_price in self.portfolio_prices:
            self.portfolio_performance.append(
                100*(porfolio_price - initial_price)/initial_price)

    def get_crypto_performance(self):
        """
        Getting the total crypto market performance day by day.
        """
        initial_price = self.crypto_prices[-1]
        for crypto_price in reversed(self.crypto_prices):
            self.crypto_performance.append(
                100*(crypto_price - initial_price)/initial_price)

    def plot_performance(self):
        """
        Plot the performance on 10 days.
        """
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        plt.plot(days, self.portfolio_performance, 'r-.')
        plt.plot(days, self.crypto_performance, 'b-.')
        plt.title(
            "Stockomatics Portfolio and Total Crypto Market Performance",
            fontweight='bold')
        plt.xlabel("Days", fontweight='bold')
        plt.ylabel("Cumulative Performance (%)", fontweight='bold')
        plt.scatter(
            days, self.portfolio_performance,
            c='r', label='Stockomatics Portfolio')
        plt.scatter(
            days, self.crypto_performance,
            c='b', label='Crypto Market Capitalization')
        plt.legend()
        plt.show()

def launch(portfolio):
    """
    launching the analysis.
    :param dict portfolio: the portfolio to analyse.
    e.g: {'btc': 2, 'eth': 12}
    """
    performance = Performance(portfolio)
    performance.load_prices()
    performance.get_porfolio_prices()
    performance.get_porfolio_performance()
    performance.load_crypto_market_cap()
    performance.get_crypto_performance()
    performance.plot_performance()


if __name__ == '__main__':
    launch(
        portfolio={'btc': 1.43,
                   'eth': 33,
                   'ada': 46000,
                   'theta': 668,
                   'dot': 31})