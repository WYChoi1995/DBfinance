from getdata import Indices, Commodities
from pandas import read_csv, merge

hscei = Indices().historical_close_price(country="hong kong", index="Hang Seng CEI",
                                         start="11/10/2011", end="11/10/2019")
stoxx50e = Indices().historical_close_price(country="germany", index="Euro Stoxx 50",
                                            start="11/10/2011", end="11/10/2019")
crudeoil = Commodities().historical_close_price(commodity="Crude Oil WTI", start="11/10/2011", end="11/10/2019")

basic_asset = merge(merge(hscei, stoxx50e, on="Date"), crudeoil, on="Date")
asset_volatility = read_csv("variance.csv", index_col="Date")

