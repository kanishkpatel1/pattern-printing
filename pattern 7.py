#      *     *
#     **    **
#    ***   ***
#   ****  ****
#  ***** *****
n=int(input("Enter the number of lines: "))
for i in range(n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    for l in range(0,n-i):
        print(" ",end="")
      
    for m in range(i+1):
        print("*",end="")
    print()
