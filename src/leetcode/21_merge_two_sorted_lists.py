# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        new_list = ListNode()

        len_l1 = len(list(iter(list1)))
        print(len_l1)

s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3

n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4

s.mergeTwoLists(node1, n1)
