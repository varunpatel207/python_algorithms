class Solution:
    def productExceptSelf(self, nums):
        answer = []

        total_product = 1
        for index, num in enumerate(nums):
            total_product = total_product * num

        for j, num in enumerate(nums):
            if num > 0:
                answer.append(int(total_product / num))
            else:
                answer.append(int())

        return answer

s = Solution()
answer = s.productExceptSelf([5,3,5])
print(answer)
