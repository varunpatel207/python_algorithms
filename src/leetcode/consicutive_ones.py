class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0
            max_ones = max(current_count, max_ones)
        return max_ones

s = Solution()
max_ones = s.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1])
print("max_ones")
print(max_ones)