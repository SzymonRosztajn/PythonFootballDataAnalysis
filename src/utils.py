def convert_to_numeric(data, column):
    data[column] = data[column].astype('category')
    category_dict = dict(enumerate(data[column].cat.categories))
    data[column] = data[column].cat.codes
    return data, {v: k for k, v in category_dict.items()}