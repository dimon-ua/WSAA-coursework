import sqlite3

class StudentDAO:
    db_file = "wsaa.db"
    connection = ""
    cursor = ""

    def __init__(self):
        self.db_file = "wsaa.db"

    def getCursor(self):
        self.connection = sqlite3.connect(self.db_file)
        self.connection.row_factory = sqlite3.Row 
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (?,?)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from student"
        cursor.execute(sql)
        results = cursor.fetchall()
        # convert Row objects to list of dicts
        return_list = [dict(row) for row in results]
        self.closeAll()
        return return_list

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "select * from student where id = ?"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return dict(result) if result else None

    def update(self, values):
        cursor = self.getCursor()
        sql = "update student set name=?, age=? where id=?"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from student where id = ?"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

studentDAO = StudentDAO()