def stringlong(s):
    n=len(s)
    if n>10:
        p=n-2
        new=(s[0]+str(p)+s[n-1])
        return new
    else:
        return s
# if __name__ == '__main__':
s=input()
print(stringlong(s))

# A. Team
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. Participants are usually offered several problems during programming contests. Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's solution.

# This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.

# Input
# The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest. Then n lines contain three integers each, each integer is either 0 or 1. If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure. The second number shows Vasya's view on the solution, the third number shows Tonya's view. The numbers on the lines are separated by spaces.

# Output
# Print a single integer — the number of problems the friends will implement on the contest.


def suretwo(n,mat):
    final=0
    for i in range(n):
        count=0
        for j in range(3):
            if mat[i][j]==1:
                count+=1
        if count>=2:
            final+=1
    return final


if __name__ == '__main__':
    n = int(input())  # Read the number of problems
    matrix = []  # Initialize an empty list to store the matrix
    
    # Iterate over each problem
    for _ in range(n):
        # Read the line and split it by spaces, then convert each part to an integer
        row = list(map(int, input().split()))
        matrix.append(row)  # Append the row to the matrix
    print(suretwo(n,matrix))


print(str(98))

