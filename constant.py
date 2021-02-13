import os

input_path = r'res/深圳市住宅小区二手住房成交参考价格表.pdf'  # input("请输入PDF文件位置：")
output_path = 'output/深圳市住宅小区二手住房成交参考价格表.xls'
baidu_map_ak = "这里填你的百度API AK码"


res_path = 'output'
data_csv = 'shenzhen_data.csv'
geo_data = "geo_data.json"
geo_data_json = os.path.join(res_path, geo_data)
shenzhen_data_csv_path = os.path.join(res_path, data_csv)
