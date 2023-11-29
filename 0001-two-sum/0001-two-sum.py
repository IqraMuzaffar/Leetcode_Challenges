class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in history:
                return[history[diff],i]
            history[n]=i
        return