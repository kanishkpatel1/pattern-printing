# A          B
# CD        EF
# GHI      JKL
# MNOP    QRST
# UVWXY  ZABCD
# EFGHIJKLMNOP
n=int(input("Enter the range : "))
ch=65
for i in range (0,n):
    for j in range(i+1):
        print(chr(ch),end="")
        ch=ch+1 
    for k in range(n-i-1):
        print(" ",end="")
    for l in range(n-i-1,0,-1):
        print(" ",end="")
    for m in range(i+1):
        print(chr(ch),end="")
        ch=ch+1
        if(ch>90):
            ch=65
    print("\r")