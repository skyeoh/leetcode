# LeetCode Practice

This repository contains my attempted solutions to LeetCode questions.

| Question | Category | Solution Highlights |
| -------- | -------- | ------------------- |
| Palindrome | |
| Merge Two Sorted Lists | Linked List | 1. Return other list if one is empty or None if both are empty <br> 2. Use head and tail for tracking: set head = list with smaller value and set tail = head <br> 3. Loop until end of at least one list, attaching smaller value and moving tail at each step <br> 4. Append remainder of unfinished list to tail, if necessary |
| Maximum Depth of Binary Tree | Tree | *Solution 1: Use recursive DFS* <br> 1. Max depth of tree = 1 + MAX(max depth of left sub-tree, max depth of right sub-tree) <br> 2. Terminating condition: max depth of tree = 0 if root == None (i.e. no tree) <br> *Solution 2: Use level-order traversal (BFS)* <br> 1. Use queue to store nodes during traversal <br> 2. Count nodes at each level to keep track of levels |
| Reverse Linked List | Linked List | *Solution 1: Use stack* <br> 1. Return list if list is empty or if list consists of single node <br> 2. Loop over list, pushing each node on stack at each step <br> 3. Pop each node back out from stack and link them together <br> *Solution 2: Iterative approach* <br> 1. Use three pointers to track previous, current and following nodes <br> 2. Loop until end of list, pointing current node to previous node and moving all pointers at each step <br> *Solution 3: Recursive approach* <br> 1. Traverse down list recursively <br> 2. Reverse node one by one on way back up |
| Longest Common Subsequence | Dynamic Programming | 1. Initialize 2-D (m+1) x (n+1) array with zeroes, where len(s1) = n and len(s2) = m <br> 2. Do nested loops to compare substrings of s1 and s2 (including empty substring): <br> - if their last characters match, i.e. s1[i] = s2[j], then LCS(i, j) = 1 + LCS(i-1, j-1) <br> - if they do not, then LCS(i, j) = MAX(LCS(i, j-1), LCS(i-1, j)) <br> 3. Return last entry of array: LCS(m+1, n+1) |
