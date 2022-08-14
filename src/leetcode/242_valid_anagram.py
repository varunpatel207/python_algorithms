class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return False if sorted(s) != sorted(t) else True

s = Solution()
print(s.isAnagram("anagram", "nagaram"))