# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        for index_i, number_i in enumerate(l1):
            for index_j, number_j in enumerate(l2):
                if index_j == index_j:
                    sum = number_i + number_j

s = Solution()
s.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])
