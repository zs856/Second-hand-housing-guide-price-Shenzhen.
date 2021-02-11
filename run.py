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
