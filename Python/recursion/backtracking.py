# N-Queens
def isSafe1(row, col, board, n):
    # check upper element
    duprow = row
    dupcol = col

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    col = dupcol
    row = duprow
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row = duprow
    col = dupcol
    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True

def solve(col, board, ans, n):
    if col == n:
        ans.append(list(board))
        return

    for row in range(n):
        if isSafe1(row, col, board, n):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            solve(col+1, board, ans, n)
            board[row] = board[row][:col] + '.' + board[row][col+1:]

def solveNQueens(n):
    ans = []
    board = ['.'*n for _ in range(n)]
    solve(0, board, ans, n)
    return ans
print(solveNQueens(4))


class Solution:
    def solve(self, col, leftRow, topDiagonal, downDiagonal, ans, board, n):
        if col == n:
            ans.append(list(board))
            return
        for row in range(n):
            if leftRow[row] == 0 and topDiagonal[n-1+col-row] == 0 and downDiagonal[row+col] == 0:
                board[row] = board[row][:col]+'Q'+board[row][col+1:]
                leftRow[row] = 1
                topDiagonal[n-1+col-row] = 1
                downDiagonal[row+col] = 1
                self.solve(col+1, leftRow, topDiagonal,
                           downDiagonal, ans, board, n)
                board[row] = board[row][:col]+'.'+board[row][col+1:]
                leftRow[row] = 0
                topDiagonal[n-1+col-row] = 0
                downDiagonal[row+col] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        leftRow = [0]*n
        topDiagonal = [0]*(2*n-1)
        downDiagonal = [0]*(2*n-1)
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, leftRow, topDiagonal, downDiagonal, ans, board, n)
        return ans
