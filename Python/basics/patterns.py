def seeding(n):
    # Write your solution here.
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print("")
seeding(3)