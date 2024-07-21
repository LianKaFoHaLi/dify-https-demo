import requests

def send_get_request(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        print("Received Markdown Data:")
        print(response.text)
    else:
        print("GET request failed, status code:", response.status_code)

def send_post_request(url, data):
    response = requests.post(url, data=data.encode('utf-8'), verify=False)
    if response.status_code == 200:
        print("POST request response:")
        print(response.json())
    else:
        print("POST request failed, status code:", response.status_code)

def send_markdown_data(url, md_data):
    response = requests.post(url, data=md_data.encode('utf-8'), verify=False)
    if response.status_code == 200:
        print("Processed Markdown Data:")
        print(response.text)
    else:
        print("Failed to process data, status code:", response.status_code)

def check_server_connection(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200 and response.json().get('message') == 'pong':
            print("Server is online and responding.")
        else:
            print("Server response unexpected:", response.text)
    except requests.exceptions.RequestException as e:
        print("Failed to connect to server:", str(e))
        
# 示例URLs
ping_url = 'https://localhost:4443/ping'
data_url = 'https://localhost:4443/data'
post_data_url = 'https://localhost:4443/postdata'
process_md_url = 'https://localhost:4443/process_markdown'

# 发送示例Markdown表格数据
markdown_data = """
| Type | Name | Note |
|------|------|------|
| A    | Tom  | Cat  |
| B    | Kitty| Cat  |
| C    | Jerry| mouse|
"""

# 调用示例
check_server_connection(ping_url)
send_get_request(data_url)
send_post_request(post_data_url, '这是一个测试数据')
send_markdown_data(process_md_url, markdown_data)
