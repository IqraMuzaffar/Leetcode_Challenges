class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        i = 0
        nums3 = []

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1
            i += 1

        # If there are remaining elements in nums1 or nums2, add them to nums3
        while p1 < m:
            nums3.append(nums1[p1])
            p1 += 1
            i += 1

        while p2 < n:
            nums3.append(nums2[p2])
            p2 += 1
            i += 1

        for i in range(m + n):
            nums1[i] = nums3[i]

        