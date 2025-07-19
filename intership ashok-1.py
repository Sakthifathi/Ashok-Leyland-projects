import mysql.connector as m
import random
con=m.connect(
    host="localhost",
    username="root",
    password="sakthi",
    database="forms")
cursor=m.connect()
print("Databse connection :",con)
form_id=random.randint(1000,10000)
name=input("enter your name")
email=input("enter your email address")
phno=int(input("enter your phone number"))
designation=input("enter your designation ")

x="INSERT INTO FORM(form_id,name,email,phno,designation)VALUES(%s,%s,%s,%s,%s)"
y=(form_id,name,email,phno,designation)
cursor=con.cursor()
cursor.execute(x,y)
con.commit()
print("You successfully added all your details in the form")
print("Your Form id is",form_id)

search_id = input("\nEnter your Form ID to see your form details: ")
cursor.execute("SELECT * FROM FORM WHERE form_id = %s", (search_id,))
result = cursor.fetchone()
if result:
    print("\n Form Details Found:")
    
    print("Name         :", result[1])
    print("Email        :", result[2])
    print("Phone Number :", result[3])
    print("Designation  :", result[4])
else:
    print("\n No form found with that Form ID.")
cursor.close()
con.close()





