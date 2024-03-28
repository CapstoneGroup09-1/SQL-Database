import mysql.connector
import json

# 从配置文件读取数据库连接信息
with open('config.json') as f:
    config = json.load(f)

# 连接到 MySQL 数据库
conn = mysql.connector.connect(**config)

def fetch_all_records(connection_info):
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(**connection_info)

        # 创建一个游标对象
        cursor = conn.cursor()

        # 执行查询
        cursor.execute('SELECT * FROM History')

        # 获取所有记录
        rows = cursor.fetchall()

        # 输出记录
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("数据库错误：", err)

    finally:
        # 关闭游标和连接
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def fetch_records_by_date(connection_info, date):
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(**connection_info)

        # 创建一个游标对象
        cursor = conn.cursor()

        # 执行查询
        query = "SELECT * FROM History WHERE DATE(RecordDate) = %s"
        cursor.execute(query, (date,))

        # 获取所有记录
        rows = cursor.fetchall()

        # 输出记录
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("数据库错误：", err)

def fetch_records_by_label(connection_info, label):
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(**connection_info)

        # 创建一个游标对象
        cursor = conn.cursor()

        # 执行查询
        query = "SELECT * FROM History WHERE label = %s"
        cursor.execute(query, (label,))

        # 获取所有记录
        rows = cursor.fetchall()

        # 如果没有查询到结果，输出"No Result"
        if not rows:
            print("No Result")
        else:
            # 输出记录
            for row in rows:
                print(row)

    except mysql.connector.Error as err:
        print("数据库错误：", err)

    finally:
        # 关闭游标和连接
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# 读取数据库连接信息
def read_config():
    with open('config.json') as f:
        return json.load(f)

# 测试该函数
if __name__ == "__main__":
    # 数据库连接信息
    connection_info = read_config()

    # 调用函数输出所有记录
    #fetch_all_records(connection_info)

    # 输入日期
    #date = '2024-03-29'  # 你的日期格式应该与数据库中存储的日期格式匹配

    # 调用函数查询指定日期的记录
    #fetch_records_by_date(connection_info, date)

    # 输入标签
    label = 'Wheat'

    # 调用函数查询指定标签的记录
    fetch_records_by_label(connection_info, label)