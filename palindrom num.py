n=int(input("enter a number: "))
temp=n
rev=0
while(n>0):
        i=n%10
        rev=rev*10+1
        n=n//10
if(temp==rev):
    print('the given number is palindrome')
else:
    print('the given number is not palindrome')
