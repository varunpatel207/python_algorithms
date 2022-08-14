
class Solution:
    def addTwoNumbers(self, l1, l2):
        for x, y in map(l1, l2):
            print(x, y)



s = Solution()
s.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])
