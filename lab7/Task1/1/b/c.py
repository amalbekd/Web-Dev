a = int(input())
b = int(input())
c = False

if(a / 10000 > 1):
    c = True

if c == True:
    if b == 1:
        print("YES")
    else:
        print("NO")
else:
    if b == 1:
        print("NO")
    else:
        print("YES")