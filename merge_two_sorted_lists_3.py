"""
-----------------------------
Name: Merge Two Sorted Lists
Source: LeetCode
-----------------------------

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

     Input: list1 = [1,2,4], list2 = [1,3,4]
     Output: [1,1,2,3,4,4]

Example 2:

    Input: list1 = [], list2 = []
    Output: []

Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    * The number of nodes in both lists is in the range [0, 50].
    * -100 <= Node.val <= 100
    * Both list1 and list2 are sorted in non-decreasing order.
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if list1 == None:
            return list2

        if list2 == None:
            return list1

        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        tail = head

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 != None:
            tail.next = list1

        if list2 != None:
            tail.next = list2

        return head


if __name__ == '__main__':

    from data_structures import ListNode

    test = Solution()

    # ========== Test 1: No input lists ==========
    merged_list = test.mergeTwoLists(None, None)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 1:", a)

    # ========== Test 2a: One input list ==========
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    merged_list = test.mergeTwoLists(node1, None)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 2a:", a)

    # ========== Test 2b: One input list ==========
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    merged_list = test.mergeTwoLists(None, node1)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 2b:", a)

    # ========== Test 3: From Example 1 ========== 
    l1_node4 = ListNode(4)
    l1_node2 = ListNode(2, l1_node4)
    l1_node1 = ListNode(1, l1_node2)

    l2_node4 = ListNode(4)
    l2_node3 = ListNode(3, l2_node4)
    l2_node1 = ListNode(1, l2_node3)

    merged_list = test.mergeTwoLists(l1_node1, l2_node1)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 3:", a)

    # ========== Test 4a ==========
    node1 = ListNode(-5)
    node2 = ListNode(10)

    merged_list = test.mergeTwoLists(node1, node2)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 4a:", a)

    # ========== Test 4b ==========
    node1 = ListNode(-5)
    node2 = ListNode(10)

    merged_list = test.mergeTwoLists(node2, node1)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 4b:", a)

    # ========== Test 5: Last value of secondary list is larger ==========
    l1_node5 = ListNode(10)
    l1_node4 = ListNode(10, l1_node5)
    l1_node3 = ListNode(4, l1_node4)
    l1_node2 = ListNode(3, l1_node3)
    l1_node1 = ListNode(1, l1_node2)

    l2_node6 = ListNode(18)
    l2_node5 = ListNode(12, l2_node6)
    l2_node4 = ListNode(4, l2_node5)
    l2_node3 = ListNode(4, l2_node4)
    l2_node2 = ListNode(3, l2_node3)
    l2_node1 = ListNode(2, l2_node2)
    
    merged_list = test.mergeTwoLists(l1_node1, l2_node1)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 5:", a)

    # =========== Test 6: Last value of primary list is larger ==========
    l1_node5 = ListNode(10)
    l1_node4 = ListNode(10, l1_node5)
    l1_node3 = ListNode(4, l1_node4)
    l1_node2 = ListNode(3, l1_node3)
    l1_node1 = ListNode(1, l1_node2)

    l2_node6 = ListNode(18)
    l2_node5 = ListNode(12, l2_node6)
    l2_node4 = ListNode(4, l2_node5)
    l2_node3 = ListNode(4, l2_node4)
    l2_node2 = ListNode(-2, l2_node3)
    l2_node1 = ListNode(-3, l2_node2)

    merged_list = test.mergeTwoLists(l1_node1, l2_node1)
    a = []
    current = merged_list
    while current != None:
        a.append(current.val)
        current = current.next
    print("Test 6:", a)







