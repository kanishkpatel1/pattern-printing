#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *
n=int(input("Enter the number of lines :"))
for i in range(0,n):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")