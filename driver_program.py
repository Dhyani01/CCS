import sqlite3
import os
from employee import Employee
from department import Department
from coordinator import Coordinator
from ccs import Ccs 
from faculty import Faculty

print("Program for Request , allotment and avaialblity ")

print("Choose which Sector you want to select ")

print("1:Department \n 2:Coordinator \n 3:Faculty")

key=input("Enter the Choice here")

if key=="1":
    password=input("Enter the key before selecting Department Sector")

    if password=="dep123":
        d=Department()
        work=input("What do you want \n 1:Request for training \n 2:Request for Fresher Training ")

        if work=="1":
            rid=input("enter request id")
            fieldid=input("Enter name of the your field id ")
            date=input("Enter the date")
            d.req_for_training(rid,fieldid,date)

        elif work=="2":
            rid=input("enter request id")
            fieldid="basic"
            date=input("Enter date here")
            d.request_for_fresher_training(fieldid,date)

        else:
            print("Wrong Choice")

    else:
        print("You have Entered Wrong Password")



elif key=="2":
    password=input("Enter the password for selecting sector of coordinator")
    if password=="cod123":
        c=Coordinator()
        work=input("What do you want \n 1:Take in login request \n 2:Request to CCS \n 3:get request for fresher")
        if work=="1":
            
            c.take_in_login_request("DFd")
        elif work=="2":

            c.request_to_ccs("fdfd")

        elif work=="3":
            c.get_request_for_fresher_training("dfdf")

        else:
            print("Wrong Choice")

    else:
        print("You have Entered Wrong Password")




elif key=="3":
    password=input("Enter the Faculty Password")

    if password=="fac123":
        f=Faculty()
        work=input("What do you want \n 1:To Appoint me \n 2:Remove appointment ")
        if work=="1":
            f.to_appoint_me("sdasd")
        elif work=="2":
            f.remove_appointment("dsd")
        else:
            print("Wrong Choice")
    else:
        print("You have Entered Wrong Password")

else:
    print("Wrong key pressed") 

