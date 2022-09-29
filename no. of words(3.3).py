b=int(input("Enter the length of the array: "))
a=[]
e=[]
for i in range(0,b):
      c=input("Enter the string: ")
      a.append(c)
      for i in range(0,b):
            d=len(a[i].split())
            e.append(d)
            print("List: ",a)
            print("Max words in a string: ",max(e))
