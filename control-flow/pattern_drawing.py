size=int(input("Enter the size of the pattern: "))
count=1
while size>=count:
    for i in range(0,size):
        print("*",end="")
    print()
    count=count+1