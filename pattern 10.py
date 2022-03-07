# *        *
# **      **
# ***    ***
# ****  ****
# **********
n=int(input("Enter the range : "))
for i in range (0,n):
    for j in range(i+1):
        print("*",end="")
    for k in range(n-i-1):
        print(" ",end="")
    for l in range(n-i-1,0,-1):
        print(" ",end="")
    for m in range(i+1):
        print("*",end="")
    print("\r")