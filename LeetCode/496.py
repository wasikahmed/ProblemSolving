# Next Greater Element I

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)        
        for i, e in enumerate(nums1):
            ans[i] = next((x for x in nums2[nums2.index(e):] if x > e), -1)

        return ans
    

soln = Solution()
print(soln.nextGreaterElement([4,1,2], [1,3,4,2]))
print(soln.nextGreaterElement([2,4], [1,2,3,4]))