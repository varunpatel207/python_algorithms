class Solution:
    def single_number_depricated(self, nums):
        count_dict = {}

        for num in nums:
            count_dict[num] = count_dict[num] + 1 if count_dict.get(num) else 1

        for key, value in count_dict.items():
            if value == 1:
                return key

    def singleNumber(self, nums):
        nums.sort()

        if len(nums) == 1:
            return nums[0]

        for index in range(0, len(nums) - 1, 2):
            if nums[index] != nums[index + 1]:
                return nums[index]

        return nums[-1]

nums = [4,1,2,1,2]
s = Solution()
number = s.singleNumber(nums=nums)
print(number)