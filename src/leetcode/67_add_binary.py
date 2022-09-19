# TODO: finish this
class Solution:
    def addBinary(self, a, b):
        max_val = max(a, b)
        min_val = min(a, b)
        min_prefix = (len(max_val) - len(min_val)) * "0"

        min_val = min_prefix + min_val if min_prefix else min_val

        carry = 0
        total = ""
        for i in range(len(max_val) - 1, -1, -1):
            for j in range(len(min_val) - 1, -1, -1):
                if i == j:
                    sum = int(max_val[i]) + int(min_val[j])
                    if sum == 2:
                        carry = 1
                        total = str(0) + total
                    elif sum == 1:
                        total = str(1) + total
                    else:
                        total = str(0) + total

                    print(max_val[i], min_val[j])

s = Solution()
s.addBinary("1010", "10")