from scipy import stats
import statsmodels.api as sm
from pandas import Series


def normality_test(x):
    print("The Test Statistic (Shapiro-Wilk) : %0.6f" % (stats.shapiro(x)[0]))
    print("p-values : %e" % (stats.shapiro(x)[1]))
    print("The Test Statistic (Kolmogorov-Smirnov): %0.6f" % (stats.kstest(x, 'norm')[0]))
    print("p-values : %e" % (stats.kstest(x, 'norm')[1]))
    print("The Test Statistic (Jarque-Bera): %0.6f" % (sm.stats.stattools.jarque_bera(x)[0]))
    print("p-values : %e" % (sm.stats.stattools.jarque_bera(x)[1]))


def get_kde_pdf(data):
    return stats.gaussian_kde(data.transpose(), bw_method='silverman')


def stepdown_valuation(kde_pdf, simulation, risk_free):
    result = []
    return_result = []

    for i in range(simulation):
        returns = 1 + kde_pdf.resample(size=504)
        result.append(returns.cumprod(axis=1))

    for i in range(simulation):
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
