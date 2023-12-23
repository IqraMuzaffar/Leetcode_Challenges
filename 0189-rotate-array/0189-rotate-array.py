class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       
        l = len(nums)
        nums2 = [0] * l  # Initialize nums2 with the same length as nums

        for i in range(len(nums)):
            index = (i + k) % l
            nums2[index] = nums[i]

        nums[:] = nums2  # Update the original list in-place