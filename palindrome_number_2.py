"""
------------------------
Name: Palindrome Number
Source: LeetCode
------------------------

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, 
    it becomes 121. Therefore it is not a palindrome.

Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # A negative integer can never be a palindrome
            return False

        xstr = str(x)
        xstrlen = len(xstr)
        front = 0
        end = xstrlen-1

        while front < end:
            if xstr[front] != xstr[end]:
                return False
            front+=1
            end-=1

        return True

if __name__ == '__main__':
    test = Solution()

    # Test 1: Palindrome
    x = 121
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 2: Negative integer
    x = -121
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 3: Non-palindrome
    x = 10
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 4: Single-digit integer
    x = 8
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 5: Long palindrome
    x = 543212345
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 6: Long non-palindrome
    x = 987654321
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 7: Long palindrome
    x = 12344321
    print('Is', x, 'a palindrome?', test.isPalindrome(x))

    # Test 8: Long non-palindrome
    x = 12345321
    print('Is', x, 'a palindrome?', test.isPalindrome(x))
