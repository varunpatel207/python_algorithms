class Solution:
    def containsDuplicate(self, nums):
        nums.sort()

        for index, num in enumerate(nums[:-1]):
            if num == nums[index + 1]:
                return True
        return False

        # num_list = set()
        #
        # for num in nums:
        #     if num in num_list:
        #         return True
        #     num_list.add(num)
        #
        # return False

nums = [9,5,6,3,9]
s = Solution()
output = s.containsDuplicate(nums=nums)
print(output)