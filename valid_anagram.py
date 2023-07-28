"""
--------------------------
Name: Valid Anagram
Source: LeetCode
--------------------------
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original
letters exactly once.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false

Constraints:
    * 1 <= s.length, t.length <= 5 * 10^4
    * s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


if __name__ == '__main__':

    test = Solution()

    # ========== Test 1: Single-letter anagrams ==========
    print('Test 1: Single-letter anagrams')
    s = "a"
    t = "a"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')

    # ========== Test 2: Single-letter NON-anagrams ==========
    print('Test 2: Single-letter NON-anagrams')
    s = "a"
    t = "z"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')

    # ========== Test 3: From Example 1 ==========
    print('Test 3: From Example 1')
    s = "anagram"
    t = "nagaram"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')

    # ========== Test 4: From Example 2 ==========
    print('Test 4: From Example 2')
    s = "rat"
    t = "car"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')

    # ========== Test 5: One string is subset of another string ==========
    print('Test 5: One string is subset of another string')
    s = "scalp"
    t = "applesauce"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')

    # ========== Test 6: Same set of characters but different occurrences ==========
    print('Test 6: Same set of characters but different occurrences')
    s = "aaaeuiiiiou"
    t = "aeiou"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')

    # ========== Test 7: Anagrams with each letter appearing only once ==========
    print('Test 7: Anagrams with each letter appearing only once')
    s = "abcdefghijklmnopqrstuvwxyz"
    t = "zyxwvutsrqponmlkjihgfedcba"
    print(s, 'vs.', t)
    print('Output:', test.isAnagram(s, t), '\n')