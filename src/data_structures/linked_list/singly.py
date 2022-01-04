class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, value):
        new_node = Node(value=value)

        current_node = self.head
        while current_node:
            if current_node.next == None:
                current_node.next = new_node
                break
            else:
                current_node = current_node.next

    def iterate(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next


node_1 = Node(1)
linked_list = LinkedList()
linked_list.head = node_1

list_1 = [2, 3, 4, 5]

for number in list_1:
    linked_list.insert_end(value=number)

linked_list.iterate()


