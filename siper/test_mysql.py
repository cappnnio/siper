
import pymysql

data = {
    'id': '2022004',
    'name': 'baolai',
    'age': 25
}

db = pymysql.connect(
    host='172.16.26.139',
    user='root',
    password='citydo@123',
    port=3306,
    database='testpy')
cursor = db.cursor()

table = 'testt'

keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    cursor.execute(sql, tuple(data.values()))
    print('Successful')
    db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
