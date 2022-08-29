n1=int(input("n1=enter the first number: "))
n2=int(input("n2=enter the second number: "))
n3=int(input("n3=enter the third number: "))
if(n1>=n2) and (n1>=n3):
    print('largest number=n1')
elif(n2>=n1) and (n2>=n3):
    print('largest number=n2')
else:
    print('largest number=n3')
