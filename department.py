import sqlite3
from coordinator import Coordinator


class Department:
    def add_department(self,name,project,deptid):
        self.name=name
        self.project=project
        self.deptid=deptid
        conn=sqlite3.connect("departments.db")
        c=conn.cursor()
        c.execute("INSERT INTO departments VALUES(self.name,self.project,self.deptid)")
        conn.commit()
        conn.close()
    def req_for_training(self,rid,fieldid,date):
        conn=sqlite3.connect("commonrequest.db")
        c=conn.cursor()
        flag="0"
        c.execute("INSERT INTO requestdata VALUES(rid,fieldid,date,flag)")
        conn.commit()
        conn.close()
        
    
    def ask_for_fresher_training(self,rid,fieldid,date):
        conn=sqlite3.connect("commonrequest.db")
        c=conn.cursor()
        flag="0"
        c.execute("INSERT INTO requestdata VALUES(rid,fieldid,date,flag)")
        conn.commit()
        conn.close()



