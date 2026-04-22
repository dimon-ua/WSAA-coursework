import sqlite3

db = sqlite3.connect('wsaa.db')
cursor = db.cursor()

sql = "select * from student where id = ?"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchone()
print(result)

sql = "update student set name=?, age=? where id=?"
values = ("Joe", 33, 1)
cursor.execute(sql, values)
db.commit()
print("update done")

sql = "delete from student where id = ?"
values = (1,)
cursor.execute(sql, values)
db.commit()
print("delete done")

db.close()