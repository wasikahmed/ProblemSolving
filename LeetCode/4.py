# Median of Two Sorted Arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = nums1 + nums2
        merged_arr.sort()

        n = len(merged_arr)
        if n % 2 != 0:
            return merged_arr[n // 2]
        return (merged_arr[(n - 1) // 2] + merged_arr[n // 2]) / 2.0
