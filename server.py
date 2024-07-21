from flask import Flask, request, jsonify
import pandas as pd
from tabulate import tabulate
from io import StringIO

app = Flask(__name__)

def markdown_to_dataframe(md_content):
    # 从Markdown格式字符串解析表格
    buffer = StringIO(md_content.strip())
    df = pd.read_csv(buffer, sep="|", skipinitialspace=True)
    df.dropna(how='all', axis=1, inplace=True)  # 清除空列
    df.columns = df.columns.str.strip()  # 清理列名空格
    return df

def dataframe_to_markdown(df):
    # 将DataFrame转换回Markdown表格
    return tabulate(df, tablefmt="pipe", headers="keys", showindex=False)

@app.route('/data', methods=['GET'])
def send_data():
    # 加载Excel文件
    df = pd.read_excel('./excel-test.xlsx')  # 修改为您的文件路径
    # 转换成Markdown格式
    markdown_table = dataframe_to_markdown(df)
    return markdown_table, 200, {'Content-Type': 'text/plain'}

@app.route('/postdata', methods=['POST'])
def receive_data():
    # 打印接收到的数据
    print(request.data.decode('utf-8'))
    return jsonify({'message': 'Data received'}), 200

@app.route('/process_markdown', methods=['POST'])
def process_markdown():
    # 接收Markdown数据
    md_data = request.data.decode('utf-8')
    # 转换为DataFrame
    df = markdown_to_dataframe(md_data)
    # 保存DataFrame为Excel文件
    df.to_excel('./processed_data.xlsx', index=False)
    # 将DataFrame转换回Markdown并返回
    md_response = dataframe_to_markdown(df)
    return md_response, 200, {'Content-Type': 'text/plain'}

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=4443, ssl_context='adhoc')
