# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insertNode(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def displayNodeValues(self):
        node_values = []
        current = self.head
        while current != None:
            node_values.append(current.val)
            current = current.next
        print(node_values)

if __name__ == "__main__":

    # Test 1 for SinglyLinkedList
    linked_list = SinglyLinkedList()
    for val in range(10):
        linked_list.insertNode(ListNode(val))
    linked_list.displayNodeValues()

    # Test 2 for SinglyLinkedList
    linked_list = SinglyLinkedList()
    for val in range(-10, 10, 2):
        linked_list.insertNode(ListNode(val))
    linked_list.displayNodeValues()
