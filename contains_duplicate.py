"""
--------------------------
Name: Contains Duplicate
Source: LeetCode
--------------------------
Given an integer array nums, return true if any value
appears at least twice in the array, and return false
if every element is distinct.

Example 1:

    Input: nums = [1,2,3,1]
    Output: true

Example 2:

    Input: nums = [1,2,3,4]
    Output: false

Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsLength = len(nums)
        if (numsLength <= 1):
            return False
        for i in range(numsLength-1):
            for j in range(i+1, numsLength):
                if nums[i] == nums[j]:
                    return True
        return False


if __name__ == '__main__':

    test = Solution()

    # ========== Test 1: Empty list ==========
    print('Test 1: Empty list')
    list1 = []
    print(list1)
    print('Result: ', test.containsDuplicate(list1), '\n')

    # ========== Test 2: List with one element ==========
    print('Test 2: List with one element')
    list2 = [10]
    print(list2)
    print('Result: ', test.containsDuplicate(list2), '\n')

    # ========== Test 3: From Example 1 ==========
    print('Test 3: From Example 1')
    list3 = [1,2,3,1]
    print(list3)
    print('Result: ', test.containsDuplicate(list3), '\n')

    # ========== Test 4: From Example 2 ==========
    print('Test 4: From Example 2')
    list4 = [1,2,3,4]
    print(list4)
    print('Result: ', test.containsDuplicate(list4), '\n')

    # ========== Test 5: From Example 3 ==========
    print('Test 5: From Example 3')
    list5 = [1,1,1,3,3,4,3,2,4,2]
    print(list5)
    print('Result: ', test.containsDuplicate(list5), '\n')