# *        * 
# **      **
# ***    ***
# ****  ****
# **********
n=int(input("Enter the number of lines: "))
sp=2*n-2
for i in range (1,n+1):
    print("*"*i+" "*sp+"*"*i,end=" ")
    sp=sp-2
    print()