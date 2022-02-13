# LINKED_LIST
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        current_node = head


s = Solution()
list_1 = [4,2,1]

head = ListNode(val=5)
for number in list_1:
    node = ListNode(val=number)

    current_node = head
    while current_node:
        if not current_node.next:
            current_node.next = node
            break
        current_node = current_node.next

max_sum = s.pairSum(head=head)