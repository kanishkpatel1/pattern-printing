#  *        * 
#   *      *
#    *    *
#     *  *
#      *
n=int(input("Enter range : "))
px=1
py=2*n-1
for i in range(0,n):
    for j in range(0,n*2):
        if(j==px or j==py):
            print("*",end=" ")
        else:
            print(" ",end="")
    px+=1
    py-=1
    print()