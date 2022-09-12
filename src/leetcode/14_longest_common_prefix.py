
class Solution:
    def longestCommonPrefix(self, strs):
        min_string = min(strs, key=len)
        strs.remove(min_string)

        prefix_str = ""
        if strs:
            for index, character in enumerate(min_string):
                for inner_index, string in enumerate(strs):
                    if string[index] != character:
                        return prefix_str

                    if inner_index == len(strs) - 1:
                        prefix_str += character
        else:
            return min_string

        return prefix_str

s = Solution()
sol = s.longestCommonPrefix(["dog"])