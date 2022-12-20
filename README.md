# LeetCode Practice

This repository contains my attempted solutions to LeetCode questions.

| Question | Category | Solution Highlights |
| -------- | -------- | ------------------- |
| Palindrome | |
| Merge Two Sorted Lists | Linked List | 1. Return other list if one is empty or None if both are empty <br> 2. Use head and tail for tracking: pick list with smaller value as head and set tail = head <br> 3. Loop until end of at least one list, attaching smaller value and moving tail at each step <br> 4. Append remainder of unfinished list to tail, if necessary |
| Maximum Depth of Binary Tree | Tree | *Solution 1: Use recursive DFS* <br> 1. Max depth of tree = 1 + MAX(max depth of left sub-tree, max depth of right sub-tree) <br> 2. Terminating condition: max depth of tree = 0 if root == None (i.e. no tree) |
