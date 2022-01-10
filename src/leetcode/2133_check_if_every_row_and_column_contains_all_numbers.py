class Solution:
    def checkValid(self, matrix):
        row_column = {}

        for n in range(len(matrix)):
            row_column[f"row_{n}"] = set(matrix[n])
            row_column[f"column_{n}"] = []
            for index in range(len(matrix)):
                if matrix[n][index] not in row_column[f"column_{n}"]:
                    row_column[f"column_{n}"].append(matrix[n][index])

        print(row_column)

        for key, value in row_column.items():
            if len(value) < len(matrix):
                return False
        return True

matrix = [[1,1,1],[1,2,3],[1,2,3]]
s = Solution()
bool_value = s.checkValid(matrix)
print(bool_value)
