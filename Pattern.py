r = int(input("Enter number of rows you want to print: "))
b = 65
for i in range(r):
    for j in range(i+1):
        print(chr(b),end="")
    b+=1
    print("\n")
