import investpy
from pandas import DataFrame


class Indices(object):
    def __init__(self):
        self.get_data = investpy.indices

    def historical_close_price(self, country, index, start, end):
        name = [index, index + "_return"]

        closeprice = self.get_data.get_index_historical_data(country=country, index=index,
                                                             from_date=start, to_date=end)["Close"]
        returns = closeprice.pct_change()

        return DataFrame({name[0]: closeprice, name[1]: returns}).dropna()


class Commodities(object):
    def __init__(self):
        self.get_data = investpy.commodities

    def historical_close_price(self, commodity, start, end):
        name = [commodity, commodity + "_return"]

        closeprice = self.get_data.get_commodity_historical_data(commodity=commodity,
                                                                 from_date=start, to_date=end)["Close"]
        returns = closeprice.pct_change()

        return DataFrame({name[0]: closeprice, name[1]: returns}).dropna()


class Bonds(object):
    def __init__(self):
        self.get_data = investpy.bonds

    def historical_close_price(self, bond, start, end):
        name = [bond, bond + "_return"]

        closeprice = self.get_data.get_bond_historical_data(bond=bond,
                                                            from_date=start, to_date=end)["Close"]
        returns = closeprice.pct_change()

        return DataFrame({name[0]: closeprice, name[1]: returns}).dropna()


def data_split(dataset, date):
    return dataset.loc[lambda data: data.index >= date]
