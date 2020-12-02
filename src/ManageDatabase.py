"""
This script is used to create and manage scheme's database
"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from EnviromentMysqlVariables import EnviromentMysqlVariables
from User import User

class ManageDatabase:
    def __init__(self):
        self.emv = EnviromentMysqlVariables()
        self.engine = self.create_connection()
        self.meta = MetaData()
        self.users_table = Table(
            'users', self.meta, 
            Column('id', Integer, primary_key = True), 
            Column('name', String(50)), 
            Column('lastname', String(50)),
            Column('birthday', Date),
            Column('cellphone', String(15)),
            Column('email', String(50)),
        )

    def create_connection(self):
        url_connection = "mysql://" + self.emv.get_mysqluser() + ":" + self.emv.get_mysqlpassword() + "@" + self.emv.get_mysqlhost() + ":" + str(self.emv.get_mysqlport()) + "/" + self.emv.get_mysqldatabase()
        engine = create_engine(url_connection,echo = True)
        return engine
    
    def close_connection(self):
        self.engine.dispose()

    def create_scheme(self):
        self.meta.create_all(self.engine)
    
    def insert_user(self, user):
        ins = self.users_table.insert().values(name = user.get_name(), lastname = user.get_lastname(), birthday = user.get_birthday(), cellphone = user.get_cellphone(), email = user.get_email())
        conn = self.engine.connect()
        result = conn.execute(ins)
    
    def delete_user(self,id):
        conn = self.engine.connect()
        stmt = self.users_table.delete().where(self.users_table.c.id == id)
        conn.execute(stmt)
    
    def update_user(self,user):
        conn = self.engine.connect()
        stmt = self.users_table.update().where(self.users_table.c.id==user.get_id()).values(name = user.get_name(), lastname = user.get_lastname(), birthday = user.get_birthday(), cellphone = user.get_cellphone(), email = user.get_email())
        conn.execute(stmt)
    
    def get_user(self,id):
        conn = self.engine.connect()
        s = self.users_table.select().where(self.users_table.c.id == id)
        result = conn.execute(s).fetchall()
        user_tmp = User(int(result[0][0]),str(result[0][1]),str(result[0][2]),str(result[0][3]),str(result[0][4]),str(result[0][5]))
        return user_tmp
    
    def get_all_users(self):
        conn = self.engine.connect()
        s = self.users_table.select()
        return conn.execute(s).fetchall()
