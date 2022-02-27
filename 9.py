a =input ("what we have ? square (s) , triangle (t) , rectangle (r)")
if "s" in a:
    a =int(input ("please enter  side of the square :"))
    Environment=a*4
    area=a*a
    print("environment is : ",Environment," and area is : ",area)
else:
    if "t" in a:
        a =int(input ("please enter  side of the triangle :"))
        Environment=a*3
        area=a*3.4
        print("environment is : ",Environment," and area is : ",area)
    else:
        if "r" in a:
            a =int(input ("please enter length :"))
            b =int(input ("please enter show :"))
            Environment=(a+b)*2
            area=a*b
            print("environment is : ",Environment," and area is : ",area) 
        else:
            print("please restart the program and do again beatween S , T , R !!!")
