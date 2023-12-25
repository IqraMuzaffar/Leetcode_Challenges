class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        small=min(len(nums1),len(nums2))
        rzlt=[]
        if(len(nums1)==small):
            subarray=nums1
            array=nums2
        else:
            subarray=nums2
            array=nums1
        for i in range(len(array)):
            if array[i] in subarray and array[i] not in rzlt:
                rzlt.append(array[i])
        return rzlt