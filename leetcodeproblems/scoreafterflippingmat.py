
def fliprow(mat, row):
    for i in range(len(mat[row])):
        if mat[row][i] == 0:
            mat[row][i] = 1
        else:
            mat[row][i] = 0
    return mat


def flipCol(mat, col):
    for i in range(len(mat)):
        if mat[i][col] == 0:
            mat[i][col] = 1
        else:
            mat[i][col] = 0
    return mat


def matrixScore(grid):
    m = len(grid)
    n = len(grid[0])
    # ensuring first el of every row has 1
    for i in range(m):
        if grid[i][0] == 0:
            grid = fliprow(grid, i)
    # checking for every col:
    for j in range(1, n):
        count0 = 0
        for i in range(m):
            if grid[i][j] == 0:
                count0 += 1
        print("beforeflip", grid)
        print(count0)
        if count0 > m-count0:
            grid = flipCol(grid, j)
            print(grid)
    # total score:
    score = 0
    for i in range(m):
        for j in range(n):
            score += grid[i][j] << (n - j - 1)
    return score


print(matrixScore([[0, 1, 1], [1, 1, 1], [0, 1, 0]]))




# Approach 2: Greedy Way(Without Modifying Input)
# Intuition
# It is often not recommended to modify the input data in place. Therefore, let us try to solve the problem without modifying the matrix.

# Let m and n be the number of rows and columns in the matrix, respectively. As we saw previously, to maximize the score, the first element of each row has to be 1. Thus, we can add 1 << (n−1)1 << (n-1)1 << (n−1) to the result m times to account for the first element of each row. This adds the contribution of the first column to the result.

# Now, we need to maximize the contribution of the remaining columns in the matrix. Similar to our previous approach, we need to count the total number of 0's and 1's in each column and flip the column if the number of 0's is greater. However, if the first element in a particular row is 0, it means that the row has been flipped previously to make the first element 1. Let us consider all possible scenarios in this regard:

# First Element	Current Element	Current Element(after potential flip)
# 0	0	1
# 0	1	0
# 1	0	0
# 1	1	1
# We can see that an element resolves to 1 only when it matches the first element in its row. Thus, to count the number of 1's in the column, we can simply count the instances where the first element is equal to the current element.

# Once we have the total number of 1's in the column, we can decide whether it is profitable to flip the column or not. We will get the maximum contribution from the column if the number of 1's is greater than the number of 0's. Thus, the number of 1's contributing to the score from that particular column would be the higher value between the counts of 0's and 1's.

# Algorithm
# Initialize m and n as the number of rows and columns in grid respectively.
# Initialize score to(1 << (n-1))*m to account for the first column of 1's.
# Iterate from the second column to the last column of the matrix. For each column:
# Initialize countSameBits as 0.
# For each element, check if it matches with the first element of the row.
# If it matches, increment countSameBits.
# Left shift 1 by the place value of the column and add it to the result max(countSameBits, m-countSameBits) times.
# Return score, which is our required result.
class Solution:
    def matrixScore(self, grid):
        m = len(grid)
        n = len(grid[0])
        # first calculate score:
        score = (1 << (n-1))*m
        # for columns:
        for j in range(1, n):
            count_1s = 0
            for i in range(m):
                if grid[i][j] == grid[i][0]:
                    count_1s += 1
            count_1s = max(count_1s, m-count_1s)
            col_score = (1 << (n-j-1))*count_1s
            score += col_score
        return score
