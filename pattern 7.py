# *****
# *****
# *****
# *****
# *****
#      *****
#      *****
#      *****
#      *****
#      *****
n=int(input("Enter the number of lines : "))
for i in range (0,n):
    for j in range(0,n):
        print("*",end="")
    print()
for m in range(n,2*n):
    for k in range(0,n):
        print(" ",end="")
    for l in range(0,n):
        print("*",end="")
    print()