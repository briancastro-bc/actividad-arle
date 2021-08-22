import pymysql

try:
    mysql = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='anuncios')
except Exception as e:
    print(f"Error: {e}")