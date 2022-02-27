im =input ("for change radian to degree enter d & for degree to radian enter r !!!")
if "d" in im :
    a =int(input ("please enter Degree for change to degree :"))
    a=(a*3.14)/180
    av = round(a,2)
    print(av)
else:
    if "r" in im :
        a =int(input ("please enter Degree for change to radian:"))
        a=(a*180)/3.145
        av = round(a,2)
        print(av)  
    else:
        print("please inter r or d instead ",im)