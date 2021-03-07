import json
import logging
import os
import time

import requests

import constant


def conduct_geocoding(query, region, page_num):
    """
    该方法用于地理编码
    :param query: 要查询的小区名
    :param region:要查询的地区，如“深圳”
    :param page_num:要查询的页码
    :return:
    """
    api_uri = "http://api.map.baidu.com/place/v2/search"
    params = {
        "query": query,
        "region": region,
        "city_limit": region,
        "page_size": 20,
        "page_num": page_num,
        "output": "json",
        "tag": "房地产",
        "ak": constant.baidu_map_ak
    }
    r = requests.get(api_uri, params=params, timeout=5)
    return json.loads(r.text)


def get_geocoding_result(query, region):
    """
    该方法用于获取查询一个小区的地理信息
    :param query:要查询的小区名
    :param region:
    :return:
    """
    page_num = 0
    fail_count = 0
    while fail_count < 3:
        try:
            res = conduct_geocoding(query, region, page_num)
            if res.get("results"):
                return res["results"][0]
            print(res.get("status"))
            status = res.get("status")
            if status == 2 or status == 302:
                logging.error("请求参数非法")
                return -1
            if status == 3:
                logging.error("权限校验失败")
                return -1
            if status == 4:
                logging.error("配额校验失败")
                return -1
            if status == 5:
                logging.error("ak不存在或者非法")
                return -1
            fail_count += 1
            time.sleep(1)
            logging.warning("重试获取")
        except Exception as e:
            logging.error(str(e))
            continue
    return -2


def get_places_in_geo_data_file():
    """
    该方法用于获取地理数据文件中所有的地方名list
    :return: 包含着地方名的list或者-1，-1代表文件未找到
    """
    if not os.path.exists(constant.geo_data_json):
        logging.error("未找到geo_data.json")
        return -1
    places = []
    geo_data_dic = json.load(constant.geo_data_json)
    for each in geo_data_dic:
        places.append(each['place'])
    return places


def get_the_geocoding_of_all_items(places):
    """
    该函数用于获取所有小区的地理编码
    
    :param places:
    :return:
    """
    print("开始获取地理数据")
    set_baidu_ak(r"D:\projects\百度ak.json")
    geo_data_list = []
    if os.path.exists(constant.geo_data_json):
        geo_data_dict = json.load(open(constant.geo_data_json))
    for place in places:
        print("当前正在获取:", place, " 的地理信息")
        res = get_geocoding_result(query=place, region="深圳")
        if res == -2:
            logging.warning("没有获取到" + place + "的地理数据")
            continue
        if res == -1:
            logging.warning("地理数据没有完全获得")
            break
        res.update({"place": place})
        print(res)
        geo_data_list.append(res)
    with open('output/geo_data.json', 'w', encoding='utf-8', ) as f:
        json.dump(geo_data_list, f, ensure_ascii=False)
    print("总共", len(geo_data_list), "条地理数据被成功获取")


def set_baidu_ak(path):
    """
    设置百度地图的ak码，ak将会从一个json文件中读取，确保字段格式为 {"al":""}
    :param path:
    :return:
    """
    if not os.path.exists(path):
        logging.error("path to access ak is not exist")
    with open(path, 'r', encoding='utf-8', ) as f:
        constant.baidu_map_ak = json.load(f)['ak']
