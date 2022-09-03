class Solution:
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

s = Solution()
sol = s.buildArray([0,2,1,5,3,4])
print(sol)
