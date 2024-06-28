def greatestNum(a,b,c):
    if(a>b and a>c):
        print(a, ' is greatest')
    elif(b>c and b>a):
        print(b, ' is greatest')
    else:
        print(c, ' is greatest')


greatestNum(8,5,6)