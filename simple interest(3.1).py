print("Enter the principle amount: ")
p=int(input())
print("Enter the number of years: ")
t=float(input())
print("Is customer senior citizen: (Y/N)")
ch=(input())
if(ch=="y"):
      r=12
else:
      r=10
      SI=(p*t*r)/100
      print("Simple interest: ",SI)

