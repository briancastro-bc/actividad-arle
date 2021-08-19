import pymysql

try:
    mysql = pymysql.connect(host='localhost', port=3310, user='root', passwd='', db='db_actividad-arle')
except Exception as e:
    print(f"Error: {e}")