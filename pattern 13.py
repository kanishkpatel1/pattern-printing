n=int(input("Enter range : "))
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