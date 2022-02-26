a =input ("please enter f for fahrenheit or c for cilios :")
b = int (input ("enter the temperatiore :"))

if "f" in a:
    l = (b-32)*5.9
else:
   l = (b*9.5)+32
print(l)
