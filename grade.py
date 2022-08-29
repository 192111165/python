s1=int(input("enter the marks of first subject: "))
s2=int(input("enter the marks of second subject: "))
s3=int(input("enter the marks of third subject: "))
s4=int(input("enter the marks of fourth subject: "))
s5=int(input("enter the marks of fifth subject: "))
avg=(s1+s2+s3+s4+s5)/5
if(avg>=90):
    print('grade=S')
elif(avg>=80):
    print('grade=A')
elif(avg>=70):
    print('grage=B')
elif(avg>=60):
    print('grade=C')
else:
    print('fail')
    

          
