from dataprocessing import basic_asset
from valuation import get_kde_pdf, stepdown_valuation, get_loss_analysis
from getdata import data_split

if __name__ == "__main__":
    kde_2011 = get_kde_pdf(basic_asset.CompoundReturn)
    kde_2014 = get_kde_pdf(data_split(basic_asset.CompoundReturn, "2014-10-11"))
    kde_2016 = get_kde_pdf(data_split(basic_asset.CompoundReturn, "2016-10-11"))

    kde_set = [kde_2011, kde_2014, kde_2016]

    simulation_result = []

    for kde in kde_set:
        simulation_result.append(stepdown_valuation(kde, risk_free=0.005, trial=10000))

    for result in simulation_result:
        get_loss_analysis(result)