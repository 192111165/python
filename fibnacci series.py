n=int(input("enter the number terms needed: "))
f1=0
f2=1
count=0
if(n<0):
    print("enter the positive integer: ")
else:
    print("the sequence of fibonacci series: ")
    while(count<n):
        print(f1)
        f3=f1+f2
        f1=f2
        f2=f3
        count=count+1
    
