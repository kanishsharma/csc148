from typing import List

class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target
        
        Preconditions:
        - You may assume each input has exactly one solution
        - May not use the same element twice
        """
        # i1 = 0
        # i2 = 1
        # while i2 < len(nums):
        #     while i1 < len(nums):
        #         if nums[i1] + nums[i2] == target:
        #             return [i1, i2]
        #         i2 += 1
        #         i1 += 1
        # return False
        nums
        i1 = 0
        i2 = len(nums) - 1 # establish two pointers
        while i1 < len(nums) and i2 > 0: # ensure the loops can keep running
            if nums[i1] + nums[i2] < target: # if lesser, increment the lowest sorted value
                i1 += 1
            elif nums[i1] + nums[i2] > target: #if greater, decrement the highest sorted value
                i2 -=1 
            elif nums[i1] + nums[i2] == target:
                val1 = nums[i1]
                val2 = nums[i2]
                return [nums.index(val1), nums.index(val2)]

    def twosumProper(self, nums: List[int], target: int) -> List[int]:
        """Proper solution for TwoSum - involves using a "hashmap", which is
        just a dictionary by my estimation
        """
        val_dict = {} # basically starts off with an empty dictionary
        for i, item in enumerate(nums): # enumerate returns the 
            remaining = target - nums[i]
            if remaining in val_dict:
                return [i, val_dict[remaining]]
            val_dict[item] = i            
    def isPalindrome(self, x: int) -> bool:
            x = str(x)
            i1 = 0
            i2 = len(x) - 1
            if len(x) < 3: # where the int is a 2 digit number
                if x[i1] != x[i2]:
                    return False
                else:
                    return True
            elif len(x) % 2 != 0:
                pass
            while i1 != i2:
                if x[i1] != x[i2]:
                    return False
                i1 += 1 
                i2 -= 1
            if x[i1] == x[i2]:
                return True
            else:
                return False
        
        # Need to keep in mind the case where i < 3
        # The case where i is an even number - need to adjust while loop for that 