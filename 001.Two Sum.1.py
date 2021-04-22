# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:24:10 2021

@author: 28076
"""
from typing import List




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums) ):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
                
#nums = [2,7,11,15]
#target = 9

#nums,target = [3,2,4], 6
nums,target = [3,3], 6

s = Solution()
print(s.twoSum(nums,target))
