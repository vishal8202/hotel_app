import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')

mycursor = mydb.cursor()
li =[]
while(True):
    print("\n please select an option")
    print("1 Tea       :   10")
    print("2 Coffee    :   20")
    print("3 Buger     :   60")
    print("4 Sandwich  :   50")
    print("5 lime      :   25")
    print("6 Generate Bill")
    print("7 view all by date")
    print("8 sum by date")
    print("9 summary inbetween two dates")
    print("10 Exit")
    ch=int(input("Enter the choice : "))
    
    if(ch==1):
        print("Added Tea")
        q = int(input("Enter the quantity : "))
        total=q*10
        li.append(total)
    elif(ch==2):
        print("Added Coffee")
        q = int(input("Enter the quantity : "))
        total=q*20
        li.append(total)

    elif(ch==3):
        print("Added Burger")
        q = int(input("Enter the quantity : "))
        total=q*60
        li.append(total)
    elif(ch==4):
        print("Added Sandwich")
        q = int(input("Enter the quantity : "))
        total=q*50
        li.append(total)
    elif(ch==5):
        print("Added lime")
        q = int(input("Enter the quantity : "))
        total=q*25
        li.append(total)
    elif(ch==6):
        print("Generating bill")
        name = input('Enter the name : ')
        phone = input('Enter the phone number : ')
        #dates = input('Enter the date in the form of yyyy-mm-d : ')
        
        count = 0
        for i in li:
           count = count + i

        amount = count
        
        sql = "INSERT INTO `bills`(`name`, `phone`, `amount`, `date`) VALUES (%s,%s,%s,now())"
        data = (name,phone,amount)
        mycursor.execute(sql,data)
        mydb.commit()
        print(name)
        print(total)
        print('Thank you!!!')
    elif ch==7:
        print("view by date selected")
        ymd = input("enter the date YYYY-MM-DD : ")
        sql = "SELECT * FROM `bills` WHERE `date`="+ymd
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif ch ==8:
        print("summary by date")
        ymd = input("Enter the date to get the total amount in the format YYYYMMDD : ")
        sql = "SELECT SUM(`amount`) FROM `bills` WHERE `date`="+ymd
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif ch==9:
        print("summary inbetween two days")
        ymd1 = input("enter the start date in YYYYMMDD : ")
        ymd2 = input("enter the end date in YYYYMMDD : ")
        sql = "SELECT SUM(`amount`) FROM `bills` WHERE `date` BETWEEN '"+ymd1+"' AND '"+ymd2+"' "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(ch==10):
        break