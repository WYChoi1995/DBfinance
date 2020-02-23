from getdata import Indices, Commodities

hscei = Indices().historical_close_price(country="hong kong", index="Hang Seng CEI",
                                         start="10/10/2011", end="11/10/2019")
stoxx50e = Indices().historical_close_price(country="germany", index="Euro Stoxx 50",
                                            start="10/10/2011", end="11/10/2019")
crudeoil = Commodities().historical_close_price(commodity="Crude Oil WTI", start="10/10/2011", end="11/10/2019")

