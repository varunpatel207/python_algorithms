# TODO: solve this
class Solution:
    def longestCommonPrefix(self, strs):
        min_length = len(min(strs, key=len))
        # for string in strs:
        print(min_length)

        common_substring = ""
        for index in range(len(min(strs, key=len))):
            for string in strs:
                common_substring += string[index]

s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])