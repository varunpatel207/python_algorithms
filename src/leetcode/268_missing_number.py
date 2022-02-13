class Solution:
    def missingNumber(self, nums):
        for i, num in enumerate(nums):
            if num not in range(0, len(nums)):
                return num


s = Solution()
missing_num = s.missingNumber([0,1])
print(missing_num)