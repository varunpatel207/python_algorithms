class Solution:
    def isValidSudoku(self, board):
        # row validate
        for row in board:
            test_row = []
            for number in row:
                if number != ".":
                    if number not in test_row:
                        test_row.append(number)
                    else:
                        print("Row fail")
                        return False

        # column validate
        for i in range(len(board)):
            test_row = []
            for j, row in enumerate(board):
                number = row[i]
                if number != ".":
                    if number not in test_row:
                        test_row.append(number)
                    else:
                        print("Column fail")
                        return False

        # 3*3 validate
        for n in [0, 3, 6]:
            grid_numbers = []
            for i in range(n, n+3):
                for j in range(0, 3):
                    number = board[i][j]
                    if number != ".":
                        if number not in grid_numbers:
                            grid_numbers.append(number)
                        else:
                            print("Grid fail")
                            return False

            # 3, 4, 5 row
            grid_numbers = []
            for i in range(n, n + 3):
                for j in range(3, 6):
                    number = board[i][j]
                    if number != ".":
                        if number not in grid_numbers:
                            grid_numbers.append(number)
                        else:
                            print("Grid fail")
                            return False

            # 6, 7, 8 row
            grid_numbers = []
            for i in range(n, n + 3):
                for j in range(3, 6):
                    number = board[i][j]
                    if number != ".":
                        if number not in grid_numbers:
                            grid_numbers.append(number)
                        else:
                            print("Grid fail")
                            return False

        return True



board = [[".","2",".",".",".",".",".",".","."],
         [".",".",".",".",".",".","5",".","1"],
         [".",".",".",".",".",".","8","1","3"],
         ["4",".","9",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".","2",".",".",".",".",".","."],
         ["7",".","6",".",".",".",".",".","."],
         ["9",".",".",".",".","4",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

s = Solution()
sol = s.isValidSudoku(board=board)

print(sol)