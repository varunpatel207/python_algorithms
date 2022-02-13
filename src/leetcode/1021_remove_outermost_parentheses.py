# TODO: solve this

# STACK

class Solution:
    def removeOuterParentheses(self, s):
        final_string = ""
        outer_stack = []
        stack = []
        for character in s:
            if character == "(" and not outer_stack:
                outer_stack.append("(")
                continue

s = Solution()
s.removeOuterParentheses("(()())(())(()(()))")