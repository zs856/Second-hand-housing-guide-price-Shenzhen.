import json
import logging
import os

from baidu_map_util import get_geocoding_result
from constant import shenzhen_data_csv_path, input_path, geo_data_json
from data_operate import shape_data, to_csv, read_data_from_csv, fuzzy_finder
from pdf_util import extract_pdf


def main():
    print("---------------深圳市住宅小区二手住房成交参考价格查询---------------")

    if not os.path.exists(shenzhen_data_csv_path):
        data = extract_pdf()
        header = data[2]
        body = data[3:]
        print("数据准备完毕，当前数据更新于2021年2月12日")
        df = shape_data(header, body)
        to_csv(df)
    else:
        df = read_data_from_csv(shenzhen_data_csv_path)
    print("请输入您想查找的小区或项目名称")
    print("如果想获取所有信息，请输入all")
    while True:
        search = input()
        if search == 'all':
            print(df)
            continue
        result = df[df['项目名称'] == search]
        if result.empty:
            print("未找到该小区")
            print("请问您要找的是以下小区么？")
            res = fuzzy_finder(user_input=search, collection=df['项目名称'])
            for place in res:
                print(place)
            continue
        print(result)


if __name__ == '__main__':
    main()
