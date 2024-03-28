import json

# 数据库连接信息
connection_info = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'gu681004',
    'database': 'CropHistory'
}


# 将连接信息写入到 config.json 文件
with open('config.json', 'w') as f:
    json.dump(connection_info, f, indent=4)

print("数据库连接信息已成功保存到 config.json 文件中。")
