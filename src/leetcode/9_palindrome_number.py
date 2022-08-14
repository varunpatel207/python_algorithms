class Solution:
    def isPalindrome(self, x):
        string_int = str(x)
        if string_int == string_int[::-1]:
            return True
        return False

s = Solution()
sol = s.isPalindrome(122)
print(sol)
