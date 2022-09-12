class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for index, par in enumerate(s):
            if par in ["(", "{", "["]:
                stack.append(par)
            else:
                if stack:
                    if (stack[-1] + par) not in ["()", "{}", "[]"]:
                        return False
                else:
                    return False
                stack.pop()
        if stack:
            return False
        return True

s = Solution()
string = "){"
sol = s.isValid(string)
print(sol)