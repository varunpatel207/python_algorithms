class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1] if s.split() else [])

s = Solution()
sol = s.lengthOfLastWord("   fly me   to   the moon  ")
print(sol)
