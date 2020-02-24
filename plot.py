import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from dataprocessing import basic_asset


def get_histogram(data, title="Distribution"):
    plt.figure(figsize=(10, 6))
    plt.title(title)
    sns.distplot(data)
    plt.show()


def get_qqplot(data, title="QQ-Plot"):
    plt.figure(figsize=(6, 6))
    plt.title(title)
    stats.probplot(data, plot=plt)
    plt.show()