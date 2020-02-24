from dataprocessing import basic_asset
from valuation import get_kde_pdf, stepdown_valuation

if __name__ == "__main__":
    compound_kde = get_kde_pdf(basic_asset.CompoundReturn)
    asset_return = stepdown_valuation(compound_kde, risk_free=0.005)
    loss_prob = len(asset_return.loc[lambda asset_return: asset_return < 0])

    print(loss_prob)
