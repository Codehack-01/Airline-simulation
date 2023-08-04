# PROJECT: AIRLINE PASSENGER LOADING SIMULATION PROGRAM PROJECT
# SIMULATION LANGUAGE: PYTHON
# ASSIGNED STUDENTS: GROUP C

chosen = []
seats = [10, 24, 33, 15, 18, 25, 46, 30]
while len(chosen) < 8:
    print('seat numbers left: ', seats)
    seat_no = eval(input('Enter a seat number: '))
    if seat_no in seats:
        if seat_no not in chosen:
            # if len(chosen)>8:
            # print("No seats Available")
            # chosen.append(t)
            # seats.remove(t)
            seat = seats.index(seat_no)
            chosen.append(seats.pop(seat))
            print('seat numbers left: ', seats)
            # print('Have a nice day and safe flight')
            # print(chosen)
            break
        elif seat_no in chosen:
            print('that seat has been picked')
    else:
        print('not a valid number')


# for i in range(1,3) :
#    print("passenger",i)
#    firstname =input("Enter first name: ")
#    lastname =input("Enter last name: ")
#    gender = input("enter gender: ")
#    age = int(input("enter age: "))
#    from random import randint
#    x = randint(10,100)
#    booking_id = ('DA'+str(x)+firstname +lastname)
#    print("your booking ID is: ",booking_id)

# unoccupied_seat = [10, 24, 33, 15, 18, 45, 26, 30]
# for i in range (1,13):
#    print("passenger",i)
#    seat_num = int(input("Enter a seat num: "))
#    while seat_num != list(unoccupied_seat):
#        correct = input("Enter a seat number: ")


# def checkPhoneNum(phone):
#    while len(phone)!=11:
#        phone = input("Enter a valid phone number")
#        return phone

# input()
import sqlite3
# connecting to the database
connection = sqlite3.connect('passengers.db')
crsr = connection.cursor()
print("connected to the database")
crsr.execute("DROP TABLE IF EXISTS passengers")
sql_command = """CREATE TABLE passengers(
First_Name TEXT,
Last_Name TEXT,
Gender TEXT,
Age INTEGER,
Booking_id VARCHAR);"""
crsr.execute(sql_command)
connection.commit()
print("table created")
# f = open('project.txt','w')
for i in range(1, 9):
    f = open('project.txt', 'a')
    print("passenger", i)
    firstname = input("Enter first name: ").title()
    lastname = input("Enter last name: ").title()
    gender = input("enter gender: ").title()
    age = int(input("enter age: "))
    from random import randint
    x = randint(10, 100)
    booking_id = ('DA'+str(x)+firstname[0] + lastname[0])
    print("your booking ID is: ", booking_id)
    f.write(firstname + "  " + lastname + "  "+gender + "  " + str(age) + "  " + booking_id+"\n")
    f.close()
    crsr.execute("""
    INSERT INTO passengers(First_Name, Last_Name, Gender, Age, Booking_id)VALUES (?,?,?,?,?)""",
                 (firstname, lastname, gender, age, booking_id))
connection.commit()
connection.close()

print("data entered successfully")
input()


# unoccupied_seat = [10, 24, 33, 15, 18, 45, 26, 30]
# for i in range (1,13):
#    print("passenger",i)
#    seat_num = int(input("Enter a seat num: "))


# import pandas as pd
# first_name = ['Samson','Mary','Mark','Andrew','Jason','Danielle','Amy','Bobby','Xavier','Franca','Bianca','Lily']
# last_name = ['Gideon','Gail','Jackson','Freid','Samuel','Gregory',
# 'Schluck','Daniel','Charles','ROse','McClark','Scarlet']
# gender = ['male','female','male','male','male','female','female','male','male','female','female','female']
# age = [34,24,22,44,21,25,23,27,30,32,41,39]
# from random import randint
# x = randint(10,100)
# bookingID = ('DA' + str(x) +str(first_name) + str(last_name))
# passtable = pd.DataFrame({'FirstName':first_name,
#                          'LastName':last_name,
#                          'Gender':gender,
#                          'Ages':age,
#                          'Booking ID':bookingID})
# print(passtable)


# sql_command = """CREATE TABLE passengers(
# First_name TEXT
# Second_name TEXT
# Sex TEXT
# Age INTEGER);"""
# crsr.execute(sql_command)
# print("table created")
# sql_command = """INSERT INTO passengers VALUES("samson","Gideon","Male",34);"""
# crsr.execute(sql_command)

input()

unoccupied_seat = [10, 24, 33, 15, 18, 45, 26, 30]
