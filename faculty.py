import sqlite3

class Faculty:

    def add_faculty_permanent(self,name,fieldid,salary):
        self.name=name
        self.fieldid=fieldid
        self.salary=salary
        conn=sqlite3.connect("facultys.db")
        c=conn.cursor()
        c.execute("INSERT INTO facultys VALUES(self.name,self.fieldid,self.salary)")
        conn.commit()
        
        dates=input("Enter the dates")
        dates=dates.split(" ")
        temp=self.name
        c.execute("CREATE TABLE "+ temp +"( date text)")           
        conn.commit()
        for i in dates:
            c.execute("INSERT INTO "+ temp + " VALUES(i)")
            conn.commit()
        
        conn.close()


    def add_faculty_visiting(self,name,fieldid,salary):
        self.name=name
        self.fieldid=fieldid
        self.salary=salary
        conn=sqlite3.connect("facultys_visting.db")
        c=conn.cursor()
        c.execute("INSERT INTO facultys VALUES(self.name,self.fieldid,self.salary)")
        conn.commit()
        dates=input("Enter the dates")
        dates=dates.split(" ")
        temp=self.name
        c.execute("CREATE TABLE "+ temp +"( date text)")           
        conn.commit()
        for i in dates:
            c.execute("INSERT INTO "+ temp + " VALUES(i)")
            conn.commit()
        
        conn.close()



    def to_appoint_me(self):
        pass


    def remove_appointment(self):
        pass
