import os
from datetime import datetime

from baidu_map_util import get_the_geocoding_of_all_items
from constant import shenzhen_data_csv_path
from data_operate_util import shape_data, to_csv, read_data_from_csv, fuzzy_finder
from pdf_util import extract_pdf

import dash_util as du
def main():
    print("---------------深圳市住宅小区二手住房成交参考价格查询---------------")

    if not os.path.exists(shenzhen_data_csv_path):
        before = datetime.now().timestamp()
        data = extract_pdf()
        time_consume = datetime.now().timestamp() - before
        print("从pdf文件读取花费：", time_consume, "秒")
        header = data[2]
        body = data[3:]
        print("数据准备完毕，当前数据更新于2021年2月12日")
        df = shape_data(header, body)
        to_csv(df)
    else:
        before = datetime.now().timestamp()
        df = read_data_from_csv(shenzhen_data_csv_path)
        time_consume = datetime.now().timestamp() - before
        print("从csv文件读取花费：", time_consume, "秒")
    du.run_server(df)
    # get_the_geocoding_of_all_items(df['项目名称'])
    # print("请输入您想查找的小区或项目名称")
    # print("如果想获取所有信息，请输入all")
    # while True:
    #     search = input()
    #     if search == 'all':
    #         print(df)
    #         continue
    #     result = df[df['项目名称'] == search]
    #     if result.empty:
    #         print("未找到该小区")
    #         print("请问您要找的是以下小区么？")
    #         res = fuzzy_finder(user_input=search, collection=df['项目名称'])
    #         for place in res:
    #             print(place)
    #         continue
    #     print(result)


if __name__ == '__main__':
    main()

