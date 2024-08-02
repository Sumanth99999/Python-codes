# 4 * 4 Pattern

n = int(input("Enter the number of hashes(#) you need:"))
for i in range(n):
    for j in range(n):
        print("#", end = "")

    print()

# Increasing Pattern

n = int(input("Enter the number of hashes(#) you need:"))
for i in range(n):
    for j in range(i+1):
        print("#", end = "")

    print()


# Decreasing Pattern


n = int(input("Enter the number of hashes(#) you need:"))
for i in range(n):
    for j in range(n-i):
        print("#", end = "")

    print()


    
