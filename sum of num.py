n=int(input("enter the number: "))
if(n<0) :
    print("enter the positive number: ")
else:
    sum=0
    while(n>0):
        sum=sum+n
        n=n-1
        print("the sum is: ",(sum))
