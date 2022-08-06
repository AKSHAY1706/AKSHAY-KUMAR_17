class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curSum = 0
        i = 0
        while i < len(nums):
            curSum += nums[i]
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
            i += 1
            
        return res
