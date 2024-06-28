def printline(n):
    if(n!=0):
        print('*'*n)
        printline(n-1)

print(printline(3))