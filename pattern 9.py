#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * * 
#     * * *
#       *
m=int(input("Enter the number of lines :"))
n=m//2
for i in range(0,n+1):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,2*(i-1)+1):
        print("*",end=" ")
    print("\r")
for i in range(n-1,0,-1):
    for k in range(0,n-i):
        print(" ",end=" ")

    for j in range(0,2*(i-1)+1):
        print("*",end=" ")
    print("\r")