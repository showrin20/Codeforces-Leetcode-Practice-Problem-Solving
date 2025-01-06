class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, cur_min, glob_max, glob_min, total = 0, 0,nums[0],nums[0], 0
        for num in nums:
            cur_max = max(num, cur_max + num)
            cur_min = min(num, cur_min + num)
            total += num
            glob_max = max(glob_max, cur_max)
            glob_min = min(glob_min, cur_min)
        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max
