from dataset import basic_asset, asset_volatility
from volatility import get_optimized_volatility_set
from pandas import DataFrame

weight, compound_vol = get_optimized_volatility_set(initial=(1, 0, 0), vol_dataset=asset_volatility)
weight_frame = DataFrame({"WTICL_weight": weight[:, 0], "HSCEI_weight": weight[:, 1], "STOXX50E_weight": weight[:, 2],
                          "CompoundVol": compound_vol})

basic_asset["CompoundReturn"] = weight_frame["WTICL_weight"].mean() * basic_asset["Crude Oil WTI_return"] + \
                                weight_frame["HSCEI_weight"].mean() * basic_asset["Hang Seng CEI_return"] + \
                                weight_frame["STOXX50E_weight"].mean() * basic_asset["Euro Stoxx 50_return"]

weight_frame.index = basic_asset.index

basic_asset.to_csv("BasicAsset.csv")
weight_frame.to_csv("WeightFrame.csv")
