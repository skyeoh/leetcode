"""
--------------------------
Name: Reverse Linked List
Source: LeetCode
--------------------------
Given the head of a singly linked list, reverse the list, and
return the reversed list.

Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:

    Input: head = [1,2]
    Output: [2,1]

Example 3:

    Input: head = []
    Output: []

Constraints:
    * The number of nodes in the list is in the range [0, 5000].
    * -5000 <= Node.val <= 5000
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        stack = []
        node = head
        while node != None:
            stack.append(node)
            node = node.next

        head = stack.pop()
        tail = head
        while stack: # stack is not empty
            tail.next = stack.pop()
            tail = tail.next

        tail.next = None
        return head


if __name__ == '__main__':

    # Definition for singly-linked list
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    test = Solution()

    # ========== Test 1: From Example 1 ==========
    print("Test 1")
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    head = node1

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  Before:", a)

    head = test.reverseList(head)

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  After:", a)

    # ========== Test 2: From Example 2 ==========
    print("Test 2")
    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    head = node1

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  Before:", a)

    head = test.reverseList(head)

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  After:", a)

    # ========== Test 3: From Example 3 ==========
    print("Test 3")
    head = None

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  Before:", a)

    head = test.reverseList(head)

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  After:", a)

    # ========== Test 4: Single node ==========
    print("Test 4")
    head = ListNode(-100)

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  Before:", a)

    head = test.reverseList(head)

    node = head
    a = []
    while node != None:
        a.append(node.val)
        node = node.next
    print("  After:", a)

