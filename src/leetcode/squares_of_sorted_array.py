class Solution:
    def sortedSquares(self, nums):
        updated_nums = []
        for num in nums:
            updated_nums.append(num ** 2)
        return sorted(updated_nums)

s = Solution()
updated_nums = s.sortedSquares(nums=[-4,-1,0,3,10])
print("updated_nums")
print(updated_nums)
