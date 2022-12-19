"""
-----------------------------------
Name: Maximum Depth of Binary Tree
Source: LeetCode
-----------------------------------
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest
leaf node.

Example 1:

    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 3

Example 2:

    Input: root = [1, null, 2]
    Output: 2

Constraints:
    * The number of nodes in the tree is in the range [0, 10^4].
    * -100 <= Node.val <= 100
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        if self.maxDepth(root.left) > self.maxDepth(root.right):
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + self.maxDepth(root.right)


if __name__ == '__main__':

    # Definition for a binary tree node
    class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    test = Solution()

    # ========== Test 1: From Example 1 ==========
    Node1 = TreeNode(3)
    Node2 = TreeNode(9)
    Node3 = TreeNode(20)
    Node4 = TreeNode(15)
    Node5 = TreeNode(7)

    Node1.left = Node2
    Node1.right = Node3
    Node3.left = Node4
    Node3.right = Node5

    print("Test 1: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 2: From Example 2 ==========
    Node1 = TreeNode(1)
    Node2 = TreeNode(2)

    Node1.right = Node2

    print("Test 2: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 3: Left-skewed tree ==========
    Node1 = TreeNode(3)
    Node2 = TreeNode(4)
    Node3 = TreeNode(5)
    Node4 = TreeNode(6)
    Node5 = TreeNode(7)

    Node1.left = Node2
    Node2.left = Node3
    Node3.left = Node4
    Node4.left = Node5

    print("Test 3: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 4: Right-skewed tree ==========
    Node1 = TreeNode(3)
    Node2 = TreeNode(4)
    Node3 = TreeNode(5)
    Node4 = TreeNode(6)

    Node1.right = Node2
    Node2.right = Node3
    Node3.right = Node4

    print("Test 4: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 5: Root only ==========
    Node1 = TreeNode(100)

    print("Test 5: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 6: Perfect tree ==========
    Node1 = TreeNode(1)
    Node2 = TreeNode(2)
    Node3 = TreeNode(3)
    Node4 = TreeNode(4)
    Node5 = TreeNode(5)
    Node6 = TreeNode(6)
    Node7 = TreeNode(7)

    Node1.left = Node2
    Node1.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node3.left = Node6
    Node3.right = Node7

    print("Test 6: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 7: Perfect tree + extra node ==========
    Node8 = TreeNode(8)
    
    Node5.right = Node8
    print("Test 7: maximum depth = ", test.maxDepth(Node1))

    # ========== Test 8: Perfect tree + a few more extra nodes =========
    Node9 = TreeNode(9)
    Node10 = TreeNode(10)
    Node11 = TreeNode(11)
    Node12 = TreeNode(12)

    Node8.left = Node9
    Node8.right = Node10
    Node10.left = Node11
    Node7.left = Node12

    print("Test 8: maximum depth = ", test.maxDepth(Node1))
