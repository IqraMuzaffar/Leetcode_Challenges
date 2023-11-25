class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list2=[]
        for item in nums:
            if item not in list2:
                list2.append(item)
        for i in range(len(list2)):
            nums[i]=list2[i]
        print(nums)    
        print(len(nums))
        return len(list2)