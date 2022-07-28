import mysql.connector
import re


def email(mail1):
    diff = mail1.split('@')
    l1 = diff[0]
    l2 = diff[1]
    if ('@' in mail1) and (l1[0].isalpha()) and ('.' in l2) and (l1[0] != '@') and (l2[0] != '.'):
        return True
    else:
        return False


def pass_(pass1):
    u, l, d, s = 0, 0, 0, 0
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if len(pass1) in range(5, 16):
        for x in pass1:
            if x.isdecimal():
                d += 1
            if x.upper() in pass1:
                u += 1
            if x.lower() in pass1:
                l += 1
            if regex.search(x) != None:
                s += 1
    if u >= 1 and l >= 1 and d >= 1 and s >= 1:
        return True
    else:
        return False


def Register(adi_db):
    mail1 = input("Enter the email: ")
    flag = True
    while flag:
        if not email(mail1):
            print("Invalid mail entered, Enter correct email")
            mail1 = input("Enter the email: ")
        else:
            flag = False

    pass1 = input("Enter the password: ")
    flag = True
    while flag:
        if not pass_(pass1):
            print("Invalid password entered, Enter correct password")
            pass1 = input("Enter the password: ")
        else:
            flag = False

    mycursor = adi_db.cursor()

    #mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(30), password VARCHAR(20))")

    sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
    val = (mail1, pass1,)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return True


def Login(db):
    print("press 1 to Login or press 2 if you forgot your password")
    lin = int(input())
    if lin == 1:
        mail_id = input("Enter the mail_id: ")
        password = input("Enter the password: ")

        mycursor = db.cursor()

        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        adr = (mail_id, password,)

        mycursor.execute(sql, adr)

        result = mycursor.fetchall()

        for x in result:
            if x in result:
                print("Welcome ", mail_id)
            else:
                print("No user found, Please Register")

    if lin == 2:
        mail1 = input("Enter your email_id: ")
        print("select 1 to retrieve password or select 2 to create new password")
        h = int(input())
        if h == 1:
            cur = db.cursor()
            passwrd = "SELECT password FROM user WHERE email = %s"
            get = (mail1,)

            cur.execute(passwrd, get)
            op = cur.fetchall()

            for x in op:
                if x in op:
                    print(*x)
                else:
                    print("Enter valid email")

        if h == 2:

            my_cursor = db.cursor()

            insertQuery = " SELECT password FROM user WHERE email = %s"
            get1 = (mail1, )

            my_cursor.execute(insertQuery, get1)

            result = my_cursor.fetchall()
            for x in result:
                if x in result:
                    print("Enter the new password: ")
                    g = input()

                    new = "UPDATE user SET password = %s WHERE email = %s"
                    val = (g, mail1,)

                    my_cursor.execute(new, val)

                    mydb.commit()
                    print("Updated Successfully")
                else:
                    print("Email does not exist, Please Register")
    return True


if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="abc",
        password="********",
        database="xyz"
    )
    while 1:
        print("select 1 to Register or Select 2 Login")
        a = int(input())
        if a == 1:
            Register(mydb)

        elif a == 2:
            Login(mydb)
        else:
            print("Invalid Input")
            break
