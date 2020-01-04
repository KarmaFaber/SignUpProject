import pymysql
#from pymysql import MySQLError

#db = pymysql.connect("database_host","username","password","database_name")

class MyDataBase(object):
    
    def __init__(self, database_host, server_username, server_password, database_name):
        self.conn=pymysql.connect(database_host, server_username, server_password, database_name)
        
    def __del__(self):
        self.conn.close() 
    
    def insert_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            #return cursor.fetchall()
     
    def select_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()
    
#----prueba conexion----
""" db=MyDataBase("localhost", "root", "", "proyect")

email="hola@g.com"
passw="nldkfg54sf6g5"
sql_insert="INSERT INTO user(email, password) VALUES ( '{}','{}')".format(email,passw)


db.insert_query(sql_insert)  """



#------prueba select-----
""" sql_select="select * from user"
myresult=db.select_query(sql_select)
for x in myresult:
    print(x) """





