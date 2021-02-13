import re

import pandas as pd

from constant import shenzhen_data_csv_path


def shape_data(header, body):
    """
    该方法用于从pdf获取数据的时候塑造dataframe形式的数据
    :param header:
    :param body:
    :return:
    """
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(body)
    df.columns = header
    return df


def to_csv(dataframe):
    '''
    该方法用于保存从PDF提取的数据到csv
    :param dataframe:
    :return:
    '''
    print("开始写入数据到csv文件")
    dataframe.to_csv(shenzhen_data_csv_path, index=False)


def read_data_from_csv(path):
    """
    该方法用于从csv文件中获取数据
    :param path:
    :return:
    """
    pd.set_option('display.max_rows', None)
    return pd.read_csv(path)


def fuzzy_finder(user_input, collection):
    """
    该方法参考于https://www.cnblogs.com/weiman3389/p/6047017.html
    :param user_input:
    :param collection:
    :return:
    """
    suggestions = []
    pattern = '.*'.join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append(item)
    return suggestions
