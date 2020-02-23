def data_split(dataset, date):
    return dataset.loc[lambda data: data.index >= date]
