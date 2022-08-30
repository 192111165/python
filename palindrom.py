str=str(input("enter a name: "))
rev=reversed(str)
if(list(str)==list(rev)):
    print('it is a palindrom')
else:
    print('it is not a palindrom')
