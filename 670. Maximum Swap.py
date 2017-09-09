'''
https://leetcode.com/problems/maximum-swap/description/

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 10^8]
'''

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(num))
        sortedNums = list(sorted(nums, reverse = True))
        for i in range(len(sortedNums) - 1):
            if nums[i] != sortedNums[i]:
                for j in range(len(nums) - i - 1):
                    if nums[len(nums) - j - 1] == sortedNums[i]:
                        idx = len(nums) - j - 1
                        break
                nums[i], nums[idx] = nums[idx], nums[i]
                return int(''.join(nums))
        return num
        
