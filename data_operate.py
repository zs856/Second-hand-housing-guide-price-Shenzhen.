import pandas as pd


def shape_data(header, body):
    pd.set_option('display.max_rows', None)
    data = []
    df = pd.DataFrame(body)
    df.columns = header
    return df
