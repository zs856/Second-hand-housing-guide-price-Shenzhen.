import json
import logging

from baidu_map_util import get_geocoding_result
from data_operate import shape_data
from pdf_util import extract_pdf


def main():
    print("---------------深圳市住宅小区二手住房成交参考价格查询---------------")
    print("开始提取数据")
    data = extract_pdf()
    header = data[2]
    body = data[3:]
    print("数据准备完毕，当前数据更新于2021年2月12日")
    df = shape_data(header, body)
    print("开始获取地理数据")
    places = df['项目名称']
    geo_data_dict = {}
    for place in places:
        print("当前正在获取:", place, " 的地理信息")
        res = get_geocoding_result(query=place, region="深圳")
        if res == -2:
            logging.warning("没有获取到"+place+"的地理数据")
            continue
        if res == -1:
            logging.warning("地理数据没有完全获得")
            break
        print(res)
        geo_data_dict.update(res)
    with open('output/geo_data.json', 'w', encoding='utf-8', ) as f:
        json.dump(geo_data_dict, f, ensure_ascii=False)
    print("总共", len(geo_data_dict), "条地理数据被成功获取")
    print("地理数据获取完毕")
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
            continue
        print(result)


if __name__ == '__main__':
    main()
