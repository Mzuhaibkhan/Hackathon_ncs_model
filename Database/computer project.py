import mysql.connector as connector
mycon=connector.connect(host="localhost",user="root",passwd="@zero1@0",database="project")
if mycon.is_connected():
    print("Successfully connected to database")
cursor=mycon.cursor()
print("1-Login\
       2-Add new user")
a=input("Enter your choice of action")
while a in (['1'] or "Login"):
    b=input("Enter the UserID")
    c=input("Enter the password")
    cursor.execute("Select*from login")
    data=cursor.fetchone()
    for i in range(len(data)+1):
        if data[0]==b and data[1]==c:
            print("Authentication Successful")
        else:
            print("Invalid details")
            break
        break
    mycon.close()
    mycon=connector.connect(host="localhost",user="root",passwd="@zero1@0",database="project")
    cursor=mycon.cursor()
    if a in ['1']:
        print("What do you want to do ?")
        print("1-Add another record\
               2-Find a record\
               3-Update a record")
        print("And in which table ")
        print("4-Member Table\
               5-Equipment Table")
        e=input("Enter your choice")
        f=input("Enter the choice of table")
        if e in (['1'] or 'Add another record'):
            if f in (['4'] or 'Member Table'):
                memberid=input("Enter the MemberID")
                member_name=input("Enter the Member_Name")
                Class=input("Enter the Class")
                mobile=input("Enter the Mobile")
                st="insert into member(MemberID,Member_Name,Class,Mobile) values('{}','{}','{}','{}')".format(memberid,member_name,Class,mobile)
                cursor.execute(st)
                mycon.commit()
                stx="select*from member"
                cursor.execute(stx)
                check=cursor.fetchone()
                for z in range(len(check)+1):
                    if check[z] in [memberid,member_name,Class,mobile]:
                        print("Record Successfullty entered")
                    else:
                        break
            if f in (['5'] or 'Equipmet Table'):
                Equipment_no=input("Enter the equipment_no")
                Equipment_Name=input("Enter the equipment_name")
                Quantity=int(input("Enter the quantity"))
                Date=input("Enter the date")
                st="insert into equipment(Equipment_no,Equipment_Name,Quantity,Date) values('{}','{},'{}','{}')".format(Equipment_no,Equipment_Name,Quantity,Date)
                cursor.execute(st)
                mycon.commit()
                stx="select*from equipment"
                cursor.execute(stx)
                check=cursor.fetchone()
                for z in range(len(check)+1):
                    if check[z] in [Equipment_no,Equipment_Name,Quantity,Date]:
                        print("Record Successfullty entered")
                    else:
                        break
        if e in (['2'] or 'Find a record'):
            if f in (['4'] or 'Member Table'):
                memberid=input("Enter the MemberID")
                st="select MemberID from member where (MemberID=memberid)"
                cursor.execute(st)
                data3=cursor.fecthone()
                print(data3)
                if data3==None:
                    print("No such record found")
                    break
            if f in(['5'] or 'Equipment Table'):
                equipment_no=input("Enter the Equipment Number")
                equipment_name=input("Enter the Equipment Name")
                ex="select Equipment_No Equipment_Name from equipment where(Equipment_No=equipment_no and Equipment_Name=equipment_name)"
                cursor.execute(ex)
                data3=cursor.fecthone()
                print(data3)
                if data3==None:
                    print("No such record found")
        if e in (['3'] or 'Update a record'):
            if f in (['4'] or 'Member Table'):
                memberid=input("Enter the MemberID")
                st="select MemberID from member where (MemberID=memberid)"
                cursor.execute(st)
                data3=cursor.fecthone()
                print(data3)
                print("Now enter the updated record")
                memberid2=input("Enter the MemberID")
                member_name2=input("Enter the Member_Name")
                Class2=input("Enter the Class")
                mobile2=input("Enter the Mobile")
                if li==None:
                        print("Please enter a valid record")
                        break
                srx="update member set MemberID=meberid2,Member_Name=member_name2,Class=Class2,Mobile=mobile2 where MemberID=memberid"
                cursor.execute(srx)
                mycon.commit()
                sup="select from member where MemberID=memberd"
                cursor.execute(sup)
                data4=cursor.fetchone()
                print(data4)
                print("The updated record, is it right?(y/n)")
                g=input("Enter the answer")
                if g==('y' or 'No'):
                    print("Ok")
                while g==('n' or 'No'):
                    print("Please enter the record again")
                    memberid=input("Enter the MemberID")
                    st="select MemberID from member where (MemberID=memberid)"
                    cursor.execute(st)
                    data3=cursor.fecthone()
                    print(data3)
                    print("Now enter the updated record")
                    memberid2=input("Enter the MemberID")
                    member_name2=input("Enter the Member_Name")
                    Class2=input("Enter the Class")
                    mobile2=input("Enter the Mobile")
                    li=[memberid2,member_name2,Class2,mobile2]
                    if li==None:
                        print("Please enter a valid record")
                        break
                    else:
                        srx="update member set MemberID=meberid2,Member_Name=member_name2,Class=Class2,Mobile=mobile2 where MemberID=memberid"
                        cursor.execute(srx)
                        mycon.commit()
                        sup="select from member where MemberID=memberd"
                        cursor.execute(sup)
                        data4=cursor.fetchone()
                        print(data4)
                        print("The updated record, is it right?(y/n)")
                        g=input("Enter the answer")
        if e in (['3'] or 'Update a record'):
            if f in (['5'] or 'Equipment Table'):
                equipment_no=input("Enter the Equipment Number")
                equipment_name=input("Enter the Equipment Name")
                ex="select Equipment_No Equipment_Name from equipment where(Equipment_No=equipment_no and Equipment_Name=equipment_name)"
                cursor.execute(ex)
                data3=cursor.fecthone()
                print(data3)
                print("Enter the updated reord now")
                Equipment_no2=input("Enter the equipment_no")
                Equipment_Name2=input("Enter the equipment_name")
                Quantity2=int(input("Enter the quantity"))
                Date2=input("Enter the date")
                li=[Equipment_no2,Equipment_Name2,Quantity2,Date2]
                if li==None:
                    print("Please enter a valid record")
                    break
                else:
                    supra="update equipment set Equipment_no=Equipment_no2,Equipment_Name=Equipment_Name2,Quantity=Quantity2,Date=Date2 where (Equipment_no=equipment_no and Equipment_Name=equipment_name)"
                    cursor.execute(supra)
                    mycon.commit()
                    sup="select from equipment where (Equipment_no=equipment_no and Equipment_Name=equipment_name)"
                    data5=cursor.fetchone()
                    print(data5)
                    print("The updated record, is it right?(y/n)")
                    g=input("Enter the answer")
                    while g==('n' or 'No'):
                        print("Please enter the record again")
                        memberid=input("Enter the MemberID")
                        st="select MemberID from member where (MemberID=memberid)"
                        cursor.execute(st)
                        data3=cursor.fecthone()
                        print(data3)
                        print("Now enter the updated record")
                        memberid2=input("Enter the MemberID")
                        member_name2=input("Enter the Member_Name")
                        Class2=input("Enter the Class")
                        mobile2=input("Enter the Mobile")
                        li=[memberid2,member_name2,Class2,mobile2]
                        if li==None:
                            print("Please enter a valid record")
                            break
                        else:
                            srx="update member set MemberID=meberid2,Member_Name=member_name2,Class=Class2,Mobile=mobile2 where MemberID=memberid"
                            cursor.execute(srx)
                            mycon.commit()
                            sup="select from member where MemberID=memberd"
                            cursor.execute(sup)
                            data4=cursor.fetchone()
                            print(data4)
                            print("The updated record, is it right?(y/n)")
                            g=input("Enter the answer")         
while a in (['2'] or "Enter a new user"):
    b=input("Enter the UseId")
    c=input("Enter the password")
    cursor.execute("Select*from login")
    data2=cursor.fetchone()
    if data2== None:
        st="Insert into login(UserId,Password) values('{}','{}')".format(b,c)
        cursor.execute(st)
        mycon.commit()
        cursor.execute("Select*from login")
        data3=cursor.fetchone()
        for i in range(len(data3)+1):
            if data3[0]==b and data3[1]==c:
                print("User Successfully added")
                j=input("Do you wish to continue(y/n)")
                if j =='y':
                    a='2'
                else:
                    a='0'
                    mycon.close()
                    break
    else:
        for i in range(len(data2)+1):
            if data2[0]==b and data2[1]==c:
                print("User already exits")
                break
            else:
                sx="Insert into login(UserId,Password) values('{}','{}')".format(b,c)
                cursor.execute(sx)
                mycon.commit()
                cursor.execute("Select*from login")
                data4=cursor.fetchone()
                if data4[0]==b and data4[1]==c:
                    print("User Successfully added")
                else:
                    print("User is not added")
                    break
            j=input("Do you wish to continue(y/n)")
            if j =='y':
               a='2'
            else:
                mycon.close()
                break
        
        
            
        




        
    
    
       
                         
                         
    


    
