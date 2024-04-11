a = int(input())

if(a % 400):
    print("YES")
elif(a % 100):
    print("NO")
elif(a % 4):
    print("YES")
else:
    print("NO")