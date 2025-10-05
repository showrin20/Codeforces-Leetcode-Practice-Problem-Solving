class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst={}
        for i in range(len(nums)):
            lst[nums[i]]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in lst and lst[diff] != i:
                return [i,lst[diff]]
                

         
        