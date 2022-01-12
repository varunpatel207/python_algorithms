# STACK

class Solution:
    def maxDepth(self, s):
        max_count = 0
        count = 0
        for character in s:
            if character == "(":
                count += 1
                max_count = max(max_count, count)
            if character == ")":
                count -= 1

        return max_count


s = Solution()
max_depth = s.maxDepth("()")
print(max_depth)
