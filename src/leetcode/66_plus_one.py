class Solution:
    def plusOne(self, digits):
        sum = digits[-1] + 1
        carry = 1 if sum == 10 else 0
        digits[-1] = 0 if sum == 10 else sum

        if len(digits) > 1:
            for index in range(len(digits) - 2, -1, -1):
                if carry == 1:
                    carry, digits[index] = (1, 0) if (digits[index] + 1 == 10) else (0, digits[index] + 1)
                else:
                    return digits

        if carry == 1:
            digits = [1] + digits

        return digits



s = Solution()
sol = s.plusOne([2,9])
print("sol")
print(sol)
