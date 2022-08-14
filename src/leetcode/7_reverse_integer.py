class Solution:
    def reverse(self, x):
        negative = -2147483648
        positive = 2147483647

        string_int = str(x)
        if string_int[0] == "-":
            reverse_int = "-" + int(string_int[::-1].replace("-", ""))
        else:
            reverse_int = int(string_int[::-1])

        if reverse_int > positive or reverse_int < negative:
            return 0
        return reverse_int

s = Solution()
reverse_int = s.reverse(2147483648)
print(reverse_int)