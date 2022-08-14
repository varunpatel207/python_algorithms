class Solution:
    def missingNumber(self, nums):
        nums.sort()
        length = len(nums)

        if nums[0] != 0:
            return 0

        for index in range(1, length):
            if nums[index] != nums[index - 1] + 1:
                return nums[index - 1] + 1

        if nums[-1] != length:
            return length

        return 0


s = Solution()
missing_num = s.missingNumber([9,6,4,2,3,5,7,0,1])
print(missing_num)