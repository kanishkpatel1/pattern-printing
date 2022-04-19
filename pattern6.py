# 1
# 23
# 456
# 7891
# 23456
n=int(input("Enter the number of lines:"))
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a=a+1
        if(a==10):
            a=1
    print()
