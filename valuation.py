from scipy import stats
from pandas import Series


def get_kde_pdf(data):
    return stats.gaussian_kde(data.transpose(), bw_method='silverman')


def stepdown_valuation(kde_pdf, trial, risk_free):
    result = []
    return_result = []

    for i in range(trial):
        returns = 1 + kde_pdf.resample(size=504)
        result.append(returns.cumprod(axis=1))

    for i in range(trial):
        if result[i][:, 89].min() >= 0.9:
            return_result.append(1.0211 * (1 + 5 * risk_free))
            continue

        elif result[i][:, 178].min() >= 0.9:
            return_result.append(1.0422 * (1 + 4 * risk_free))
            continue

        elif result[i][:, 252].min() >= 0.85:
            return_result.append(1.0633 * (1 + 3 * risk_free))
            continue

        elif result[i][:, 341].min() >= 0.8:
            return_result.append(1.0844 * (1 + 2 * risk_free))
            continue

        elif result[i][:, 430].min() >= 0.75:
            return_result.append(1.1055 * (1 + risk_free))
            continue

        elif result[i][:, 503].min() >= 0.7:
            return_result.append(1.1266)
            continue

        else:
            if result[i][:502].min() >= 0.5:
                return_result.append(1.1266)
            else:
                return_result.append(result[i][:, 503].min())

    return_series = 100 * Series(return_result) - 100

    return return_series


def get_loss_analysis(simulation_result):
    loss_simulation = simulation_result.loc[lambda result: result < 0]
    loss_prob = len(loss_simulation) / len(simulation_result)
    maximum_loss = loss_simulation.min()

    print("Loss Probability: {}%".format(100*loss_prob))
    print("Maximum Loss: {}%".format(maximum_loss))
