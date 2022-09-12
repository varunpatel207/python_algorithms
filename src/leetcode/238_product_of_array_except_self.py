# TODO: Finish this

class Solution:
    def productExceptSelf(self, nums):
        answer_array = [1]
        for index, num in enumerate(nums[1:]):
            answer_array.append(num * answer_array[-1])

        for index, num in enumerate(nums[::-1]):
            pass
        return answer_array

s = Solution()
answer = s.productExceptSelf([1,1,1,1,1,0,1])
print(answer)
