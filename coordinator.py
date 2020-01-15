import sqlite3
from ccs import Ccs

class Coordinator:
    def add_yourself(self,name,cid):
        self.name=name
        self.cid=cid
        conn=sqlite3.connect("coordinators.db")
        c=conn.cursor()
        c.execute("INSERT INTO coordinators VALUES(self.name,self.cid)")
        conn.commit()
    def take_in_login_request(self,fieldid,date):
        conn=sqlite3.connect("commonrequest.db")
        c=conn.cursor()
        c.execute("SELECT fieldid FROM requestdata WHERE flag='0'")
        var=c.fetchall()
        for var1 in var:
            for var2 in var1:
                variable_1=var2
        c.execute("SELECT date FROM requestdata WHERE flag='0'")
        var=c.fetchall()
        for var1 in var:
            for var2 in var1:
                variable_2=var2
 
    def allot_faculty(self,variable_1,variable_2):
        conn=sqlite3.connect("facultys.db")
        c=conn.cursor()
        c.execute("SELECT name FROM facultys WHERE fieldid=variable_1")






