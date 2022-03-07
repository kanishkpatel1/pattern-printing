
#      *     
#     *  *
#    *    *
#   *      *
#  *        *
#   *      *
#    *    *
#     *  *
#      *
m=int(input("Enter range : "))
n=m//2
px=n
py=n
for i in range(0,n):
    for j in range(0,2*n):
        if(j==px or j== py):
            print("*",end=" ")
        else:
            print(" ",end="")
    px-=1
    py+=1
    print()
    
n=n-1
px=2
py=2*n
for i in range(0,n):
    for j in range(0,(n+1)*2-1):
        if(j==px or j==py):
            print("*",end=" ")
        else:
            print(" ",end="")
    px+=1
    py-=1
    print()










