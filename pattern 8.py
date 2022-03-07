#     *
#    **
#   ***
#  ****
# *****
#      *****
#      ****
#      ***
#      **
#      *

n=int(input("Enter the number of lines : "))
for i in range (n):
    for a in range(n-i,0,-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for k in range(0,n):
        print(" ",end="")
        
    for l in range(i,n):
        print("*",end="")
    for m in range(1,i):
        print(" ",end="")
    print()
