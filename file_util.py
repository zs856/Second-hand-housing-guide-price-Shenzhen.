import json
import logging
import os
from datetime import datetime

import constant





def save_data(data):
    '''
    该方法用于保存地理数据
    :param data:
    :return:
    '''
    date_str = datetime.now().strftime('%Y-%m-%d')
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, date_str + '.json')
    with open(file_path, 'w') as f:
        json.dump(data, f)
