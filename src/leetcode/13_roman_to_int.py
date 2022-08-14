class Solution:
    def romanToInt(self, s):
        dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                 "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        exception_list = ["IV", "IX", "XL", "XC", "CD", "CM"]
        total = 0
        for exception in exception_list:
            if exception in s:
                total += dict1[exception]
                s = s.replace(exception, "", 1)

        for character in s:
            total += dict1[character]

        return total

s = Solution()
total = s.romanToInt("MCMXCIV")
print(total)