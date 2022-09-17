class Solution:
    def removeDuplicates(self, nums):
        left = 0

        if nums:
            if len(nums) == 1:
                return 1
            else:
                for index, num in enumerate(nums):
                    if index > 0:

                        print(index, num, nums[index - 1], num != nums[index - 1], left)
                        if num != nums[index - 1]:
                            nums[left] = num
                            left += 1
                    else:
                        left += 1

        return left





s = Solution()
sol = s.removeDuplicates([1,1,1,0])
print(sol)

# [0,0,1,1,1,2,2,3,3,3,4]

# 0 last
# [0,1,1,1,2,2,3,3,3,4,0]

#
# [0,1,1,1,2,2,3,3,3,4,0]

