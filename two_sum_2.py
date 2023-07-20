"""
--------------------------
Name: Two Sum
Source: LeetCode
--------------------------
Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    * 2 <= nums.length <= 10^4
    * -10^9 <= nums[i] <= 10^9
    * -10^9 <= target <= 10^9
    * Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than
O(n^2) time complexity?
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


if __name__ == '__main__':

    test = Solution()

    # ========== Test 1: From Example 1 ==========
    print('Test 1: From Example 1')
    nums = [2, 7, 11, 15]
    target = 9
    print("nums =", nums, ", target =", target)
    print('Output:', test.twoSum(nums, target), '\n')

    # ========== Test 2: From Example 2 ==========
    print('Test 2: From Example 2')
    nums = [3, 2, 4]
    target = 6
    print("nums =", nums, ", target =", target)
    print('Output:', test.twoSum(nums, target), '\n')

    # ========== Test 3: From Example 3 ==========
    print('Test 3: From Example 3')
    nums = [3, 3]
    target = 6
    print("nums =", nums, ", target =", target)
    print('Output:', test.twoSum(nums, target), '\n')

    # ========== Test 4: Repeated values that are part of solution ==========
    print('Test 4: Repeated values that are part of solution')
    nums = [2, -7, 10, -9, -7, 20, -1]
    target = -14
    print("nums =", nums, ", target =", target)
    print('Output:', test.twoSum(nums, target), '\n')

    # ========== Test 5: Repeated values that are not part of solution ==========
    print('Test 5: Repeated values that are not part of solution')
    nums = [20, 3, 20, 2, 20, 4]
    target = 6
    print("nums =", nums, ", target =", target)
    print('Output:', test.twoSum(nums, target), '\n')

    # ========== Test 6: Sum of positive and negative values ==========
    print('Test 6: Sum of positive and negative values')
    nums = [1, -2, 3, -4, 5, -6, 7, -8, 21, -10]
    target = 11
    print("nums =", nums, ", target =", target)
    print('Output:', test.twoSum(nums, target), '\n')