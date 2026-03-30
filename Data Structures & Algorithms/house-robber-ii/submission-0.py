from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # Rob excluding the first house or excluding the last house
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))
    
    # Helper function to solve the linear house robber problem
    def rob_linear(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        
        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr
            
        return prev1
