s1 = int(input("Enter number 1: "))
s2 = int(input("Enter number 2: "))
s3 = int(input("Enter number 3: "))

avr = (s1+s2+s3)/300*100

if(s1>33 and s2>33 and s3>33 and avr>=40):
    print('passed ',avr)
else:
    print('failed',avr)
    