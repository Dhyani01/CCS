import sqlite3
import os
from employee import Employee
from department import Department
from coordinator import Coordinator
from ccs import Ccs 
from faculty import Faculty
print("Program for Database Creation or Registration ")

print("Choose which database you want to Update or Register ")

print("1:Employee \n 2:Department \n 3:Coordinator \n 4:Faculty")

key=input("Enter the Choice here")

if key=="1":
    password=input("Enter the key before updating employee database")

    if password=="emp123":
        e=Employee()
        work=input("What do you want \n 1:Add Employee \n 2:Remove Employee \n 3:Update Employee ")

        if work=="1":
            name=input("Enter name of the Employee")
            type_=input("Enter the Employee Type")
            empid=input("Enter Employee ID")
            deptid=input("Enter Department ID")
            e.add_employee(name,type_,empid,deptid)

        elif work=="2":
            name=input("Enter name of the Employee")
            empid=input("Enter Employee ID")
            e.remove_employee(name,empid)

        elif work=="3":
            type_=input("Enter the type of the Employee")
            empid=input("Enter the empid of the Employee")
            e.update_employee_type(type_,empid)

        else:
            print("Wrong Choice")

    else:
        print("You have Entered Wrong Password")



elif key=="2":
    password=input("Enter the password for Updating Database of Department")

    if password=="dept123":
            d=Department()
            name=input("Enter name of the department")
            project=input("Enter the name of the project")
            deptid=input("Enter the Department ID")
            d.add_department(name,project,deptid)

    else:
        print("You have Entered Wrong Password")



elif key=="3":
    password=input("Enter the password for Updating Database of coordinator")

    if password=="cod123":
        c=Coordinator()
        name=input("Enter Name of the Coordinator")
        cid=input("Enter your Coordinator Id")
        c.add_yourself(name,cid)

    else:
        print("Wrong Password Entered")


elif key=="4":
    password=input("Enter the Faculty Password")

    if password=="fac123":
        work=input("Which type of faculty you want to enter 1:Permanent Faculty \n 2:Visiting Faculty")
        f=Faculty()
        if work=="1":
            name=input("Enter Faculty name here")
            fieldid=input("Enter field Id here")
            salary=input("Enter Your Salary")
            f.add_faculty_permanent(name,fieldid,salary)
        elif work=="2":     
            name=input("Enter Faculty name here")
            fieldid=input("Enter field Id here")
            salary=input("Enter Your Salary")
            f.add_faculty_visiting(name,fieldid,salary)
        else:
            print("Wrong Choice")
    else:
        print("You have Entered Wrong Password")

else:
    print("Wrong key pressed") 
