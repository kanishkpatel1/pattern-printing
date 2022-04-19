# *************
# *           *
# *           *
# *           *
# *************
n=int(input("Enter the number of lines: "))
for i in range (0,n):
    for j in range(0,3*n-2):
        if(i==0 or i==n-1 or j==0 or j==3*n-3):
            print("*",end="")
        else:
            print(" ",end="")
    print("\r")