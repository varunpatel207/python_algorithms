class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result

s = Solution()
sol = s.lengthOfLongestSubstring(" ")
print(sol)