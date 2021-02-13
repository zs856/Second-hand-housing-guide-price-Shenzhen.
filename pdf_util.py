import pdfplumber
import constant


def extract_pdf():
    print("开始提取数据")
    data = []
    pdf = pdfplumber.open(constant.input_path)
    for page in pdf.pages:
        for table in page.extract_tables():
            for row in table:
                data.append(row)
    pdf.close()
    return data
