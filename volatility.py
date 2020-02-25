from scipy.optimize import minimize
from numpy import zeros, sqrt, array


def get_covmat(i, vol_dataset):
    columns = vol_dataset.columns
    values = []

    for column in columns:
        values.append(vol_dataset[column][i])

    covmat = zeros((3, 3))
    covmat[0][0] = values[0] ** 2
    covmat[1][1] = values[1] ** 2
    covmat[2][2] = values[2] ** 2
    covmat[0][1] = covmat[1][0] = values[3]
    covmat[0][2] = covmat[2][0] = values[4]
    covmat[1][2] = covmat[2][1] = values[5]

    return covmat


def get_volatility(weight, i, vol_dataset):
    return sqrt(weight.T @ get_covmat(i, vol_dataset) @ weight)


def minimize_volatility(initial, i, vol_dataset):
    bound = (0, 1)
    bounds = (bound, bound, bound)
    cons = ({'type': 'eq', 'fun': sum_ratios})
    result = minimize(get_volatility, x0=initial, args=(i, vol_dataset), bounds=bounds, method='SLSQP',
                      constraints=cons)

    return result.x, result.fun


def sum_ratios(ratios):
    return ratios.sum() - 1


def get_optimized_volatility_set(initial, vol_dataset):
    result_x = []
    result_y = []

    for i in range(len(vol_dataset)):
        result_x.append(minimize_volatility(initial=initial, i=i, vol_dataset=vol_dataset)[0])
        result_y.append(minimize_volatility(initial=initial, i=i, vol_dataset=vol_dataset)[1])

    return array(result_x), array(result_y)
