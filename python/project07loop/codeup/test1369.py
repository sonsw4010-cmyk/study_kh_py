x = input().split()
n = int(x[0])
k = int(x[1])
        
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or k == 1:
            print("*", end="")
        else :
            if (i + j) % k == 0:
                print("*", end="")
            else:
                print(" ", end="")
    print()