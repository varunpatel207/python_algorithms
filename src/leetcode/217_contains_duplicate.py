class Solution:
    def containsDuplicate(self, nums):
        num_list = set()

        for num in nums:
            if num in num_list:
                return True
            num_list.add(num)

        return False

nums = [1,5,6,3,9,1]
s = Solution()
output = s.containsDuplicate(nums=nums)
print(output)