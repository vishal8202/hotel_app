li =[]
while(True):
    print("\n please select an option")
    print("1 Tea       :   10")
    print("2 Coffee    :   20")
    print("3 Buger     :   60")
    print("4 Sandwich  :   50")
    print("5 lime      :   25")
    print("6 Generate Bill")
    print("7 Exit")
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
        print(total)
    elif(ch==7):
        break