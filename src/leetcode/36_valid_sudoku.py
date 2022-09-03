class Solution:
    def isValidSudoku(self, board):

        # row
        for index, row in enumerate(board):
            local_row = []
            for number in row:
                if number in local_row and number != ".":
                    return False
                else:
                    if number not in local_row:
                        local_row.append(number)

        # column
        for i in range(len(board)):
            local_row = []
            for j in range(len(board)):
                number = board[j][i]
                if number in local_row and number != ".":
                    return False
                else:
                    if number not in local_row:
                        local_row.append(number)

        # 3*3 grid
        for i in range(len(board)):
            local_row = []
            for j in range(3):
                local_row.append(board[j][i])
            print(local_row)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
, ["6", ".", ".", "1", "9", "5", ".", ".", "."]
, [".", "9", "8", ".", ".", ".", ".", "6", "."]
, ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
, ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
, ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
, [".", "6", ".", ".", ".", ".", "2", "8", "."]
, [".", ".", ".", "4", "1", "9", ".", ".", "5"]
, [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()
sol = s.isValidSudoku(board=board)
print(sol)
