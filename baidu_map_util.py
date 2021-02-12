import json
import logging
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
    该方法用于获取查询每个小区的地理信息
    :param query:要查询的小区名
    :param region:
    :return:
    """
    page_num = 0
    fail_count = 0
    while fail_count < 3:
        res = conduct_geocoding(query, region, page_num)
        if res.get("results"):
            return res["results"][0]
        status = res.get("status")
        if status == 2:
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
    return -2
