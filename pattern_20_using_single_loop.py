#     *  
#    * *
#   * * *
#  * * * *
# * * * * *

n=int(input("Enter the numbr of lines: "))
for i in range (1,n+1):
    print(" "*(n-i)+ "* "*i,end=" ")
    print()