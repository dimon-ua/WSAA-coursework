import mysql.connector

class StudentDAO:
    host = "localhost"
    user = "root"
    password = ""
    database = "wsaa"
    connection = None
    cursor = None

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "wsaa"

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        if self.connection:
            self.connection.close()
        if self.cursor:
            self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql = "insert into student (name, age) values (%s, %s)"
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
        sql = "update student set name = %s, age = %s where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

studentDAO = StudentDAO()