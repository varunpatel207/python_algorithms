class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node

    def iterate(self):
        current_node = self.head
        while current_node:
            print (current_node.value)
            current_node = current_node.next

    def insert_end(self, value):
        new_node = Node(value)

        current_node = self.head
        while current_node:
            if current_node.next == None:
                current_node.next = new_node
                new_node.prev = current_node
                break
            else:
                current_node = current_node.next

doubly_linked_list = DoublyLinkedList()
head_node = Node(1)
doubly_linked_list.head = head_node

list_1 = [2, 3, 4, 5]

for number in list_1:
    doubly_linked_list.insert_end(value=number)

doubly_linked_list.iterate()