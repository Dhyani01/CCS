import sqlite3

class Employee:
    def add_employee(self,name,type_,empid,deptid):
        self.name=name
        self.type_=type_
        self.empid=empid
        self.deptid=deptid
        conn=sqlite3.connect("employees.db")
        c=conn.cursor()
        c.execute("INSERT INTO employees VALUES(self.type_,self.name,self.empid,self.deptid)")
        conn.commit()
    def remove_employee(self,name,empid):
        self.name=name
        self.empid=empid
        conn=sqlite3.connect("employees.db")
        c=conn.cursor()
        c.execute("DELETE from employees WHERE name=self.name and empid=self.empid")
        conn.commit()
    def update_employee_type(self,type_,empid):
        self.type=type_
        self.empid=empid
        conn=sqlite3.connect("employees.db")
        c=conn.cursor()
        c.execute("UPDATE employees SET type=self.type WHERE empid=self.empid")
        conn.commit()



