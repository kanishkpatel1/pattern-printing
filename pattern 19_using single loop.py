# ********** 
# ****  ****
# ***    ***
# **      **
# *        *

n=int(input("Enter the number of lines: "))
sp=0
for i in range (n,0,-1):
    print("*"*i+" "*sp+"*"*i,end=" ")
    sp=sp+2
    print()