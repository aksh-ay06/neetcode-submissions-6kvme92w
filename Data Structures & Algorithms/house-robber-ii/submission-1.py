class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]

        def linear_rob(houses):
            prev_max = 0
            curr_max = 0
            for x in houses:
                temp = max(curr_max, prev_max + x)
                prev_max = curr_max
                curr_max = temp
            return curr_max

        option_1 = linear_rob(nums[:-1])
        option_2 = linear_rob(nums[1:])

        return max(option_1, option_2)