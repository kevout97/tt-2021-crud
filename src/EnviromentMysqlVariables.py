"""
This class y used to save value of enviroment variables
"""

import os

class EnviromentMysqlVariables:
    def __init__(self):
        self.set_mysqldatabase(os.environ['TT_DBDATABASE'])
        self.set_mysqlhost(os.environ['TT_DBHOST'])
        self.set_mysqlport(int(os.environ['TT_DBPORT']))
        self.set_mysqluser(os.environ['TT_DBUSER'])
        self.set_mysqlpassword(os.environ['TT_DBPASSWORD'])

    def get_mysqldatabase(self):
        return self.mysqldatabase

    def get_mysqlhost(self):
        return self.mysqlhost
    
    def get_mysqlport(self):
        return self.mysqlport
    
    def get_mysqluser(self):
        return self.mysqluser
    
    def get_mysqlpassword(self):
        return self.mysqlpassword

    def set_mysqldatabase(self,mysqldatabase = "tt-2021-cruddb"):
        self.mysqldatabase = mysqldatabase 

    def set_mysqlhost(self,mysqlhost = "localhost"):
        self.mysqlhost = mysqlhost
    
    def set_mysqlport(self, mysqlport = 3306):
        self.mysqlport = mysqlport
    
    def set_mysqluser(self, mysqluser = "user") :
        self.mysqluser = mysqluser
    
    def set_mysqlpassword(self, mysqlpassword = "password"):
        self.mysqlpassword = mysqlpassword