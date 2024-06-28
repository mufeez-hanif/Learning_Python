n = int(input("Enter number: "))
if(n<=1):
    print('Number is Prime')
    exit()

i= 2
check = True;
while(i<n):
    if(n%i==0):
        print('Number is not Prime')
        check = False
        break       # when break statement is called, else block will not be executed
    i+=1
else:  
    print('Number is Prime')