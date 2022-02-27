a =int(input ("please enter first number :"))
b =int(input ("please enter sec number :"))
c =int(input ("please enter third number :"))
if a+b>c:
    if a+c>b:
        if c+b>a:
            print("we can do that :)")
        else:
            print("we want by cant!! :(")
    else:
        print("we want by cant!! :(")
else:
    print("we want by cant!! :(")