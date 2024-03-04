import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="bank")

def open_account():
    n=input("Enter account holder name: ")
    acc=input("Enter Account No: ")
    db=input("Enter DOB: ")
    cn=input("Enter Mobile Number: ")
    add=input("Enter current residing adress: ")
    ob=int(input("Enter Opening Balance: "))
    data1=(n,acc,db,cn,ob,add)
    data2=(n,acc,ob)
    sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    c=mydb.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    mydb.commit()
    print("Data entered successfully")
    main()



def deposit_amount():
    am=int(input("Enter amount to deposit: "))
    acc=input("Enter account no: ")
    a="select total_balance from amount where accno=%s"
    data=(acc,)#creating a tuple
    c=mydb.cursor()
    c.execute(a,data)
    result=c.fetchone()
    t=result[0]+am
    sql=('update amount set total_balance=%s where accno=%s')
    d=(t,acc)
    c.execute(sql,d)
    mydb.commit()
    main()




def withdraw():

    am=int(input("Enter amount: "))
    acc=input("Enter account no: ")
    a='select total_balance from amount where accno=%s'
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    result=c.fetchone()
    t=result[0]-am
    sql=('update amount set total_balance=%s where accno=%s')
    d=(t,acc)
    c.execute(sql,d)
    mydb.commit()
    main()




def balance():
    acc=input("Enter the account no: ")
    a='select * from amount where accno=%s'
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    result=c.fetchone()
    print("Balance for account: ",acc," is",result[-1])
    main()
 
def display():
    acc=input("Enter account no: ")
    a='select * from account where accno=%s'
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    result=c.fetchone()
    for i in result:
        print(i)
    main()


def close_account():
    acc=input("Enter account no:")
    sql1='delete from account where accno=%s'
    sql2='delete from amount where accno=%s'
    data=(acc,)
    c=mydb.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    mydb.commit()
    main()

#main function for choosing options

def main():
    print('''
          1. OPEN A NEW ACCOUNT
          2. DEPOSIT AMOUNT
          3. WITHDRAW AMOUNT
          4. BALANCE ENQUIRY
          5. DISPLAY ACCOUNT HOLDER DETAILS
          6. CLOSE AN ACCOUNT
          ''')
    choice=input("Enter the choice no: ")
    if(choice=='1'):
        open_account()
    elif(choice=='2'):
        deposit_amount()
    elif(choice=='3'):
        withdraw()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        display()
    elif(choice=='6'):
        close_account()
    else:
        print("INVALID CHOICE.....")
        main()
main()
    