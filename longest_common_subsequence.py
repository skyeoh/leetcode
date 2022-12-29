"""
---------------------------------
Name: Longest Common Subsequence
Source: LeetCode
---------------------------------

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining
characters.

* For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

    Input: text1 = "abcde", text2 ="ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

    Input: text1 = "abc", text = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    * 1 <= text1.length, text2.length <= 1000
    * text1 and text2 consist of only lowercase English characters.
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        if n == 0 or m == 0:
            return 0
        LCS = [(n+1)*[0] for i in range(m+1)]
        for j in range(1, m+1):
            for i in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    LCS[j][i] = 1 + LCS[j-1][i-1]
                else:
                    LCS[j][i] = max(LCS[j][i-1], LCS[j-1][i])
        return LCS[m][n]


if __name__ == '__main__':

    test = Solution()

    # ========== Test 1: One empty string ==========
    text1 = ""
    text2 = "abcde"
    print('Test 1a:', test.longestCommonSubsequence(text1, text2))
    print('Test 1b:', test.longestCommonSubsequence(text2, text1))

    # ========== Test 2: Two empty strings ==========
    text1 = ""
    text2 = ""
    print('Test 2:', test.longestCommonSubsequence(text1, text2))

    # ========== Test 3: From Example 1 ==========
    text1 = "abcde"
    text2 = "ace"
    print('Test 3a:', test.longestCommonSubsequence(text1, text2))
    print('Test 3b:', test.longestCommonSubsequence(text2, text1)) # switch parameters

    # ========== Test 4: From Example 2 ==========
    text1 = "abc"
    text2 = "abc"
    print('Test 4:', test.longestCommonSubsequence(text1, text2))

    # ========== Test 5: From Example 3 ==========
    text1 = "abc"
    text2 = "def"
    print('Test 5:', test.longestCommonSubsequence(text1, text2))

    # ========== Test 6: With repeating characters ==========  
    text1 = "tuvvwxyyyz"
    text2 = "qqrsuuvxyy"
    print('Test 6:', test.longestCommonSubsequence(text1, text2)) # answer: 5

    # ========== Test 7: With sentences ========== 
    text1 = "I love apples, oranges and pears"
    text2 = "She loves oranges and pears"

    print('Test 7:', test.longestCommonSubsequence(text1, text2)) # answer: 24
