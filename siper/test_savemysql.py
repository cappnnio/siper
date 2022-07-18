import pymysql

db = pymysql.connect(
    host='172.16.26.139',
    user='root',
    password='citydo@123',
    port=3306,
    database='testpy')
cursor = db.cursor()

id = '2022003'
name = 'bobo2'
age = 22




sql = 'INSERT INTO testt (id,name,age) values (%s,%s,%s)'
try:
    cursor.execute(sql, (id, name, age))
    db.commit()
except:
    db.rollback()
db.close()
