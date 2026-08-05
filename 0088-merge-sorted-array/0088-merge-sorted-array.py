class Solution:
    def merge(self, nums1, m, nums2, n):

        # Take only the valid elements from nums1
        arr1 = nums1[:m]

        # Merge both arrays
        merged = arr1 + nums2

        # Sort the merged array
        merged.sort()

        # Copy back into nums1
        for i in range(m + n):
            nums1[i] = merged[i]