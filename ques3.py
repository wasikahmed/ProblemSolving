from typing import List

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        def find_subsequence_sum(idx: int, current_sum: int, arr: List[int], target: int) -> bool:
            # base case
            if current_sum == target:
                return True
            if idx == len(arr) or current_sum > target:
                return False

            # Choice 1: skip element
            if find_subsequence_sum(idx + 1, current_sum, arr, target):
                return True

            # Choice 2: take element
            if find_subsequence_sum(idx + 1, current_sum + arr[idx], arr, target):
                return True

            return False

        res = []
        n = len(nums)
        for x in range(1, n + 1):
            capped_arr = [min(num, x) for num in nums]
            possible = find_subsequence_sum(0, 0, capped_arr, k)
            res.append(possible)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsequenceSumAfterCapping([4,3,2,4], 5))  # [False, False, True, True]
    print(solution.subsequenceSumAfterCapping([1,2,3,4,5], 3)) # [True, True, True, True, True]
    print(solution.subsequenceSumAfterCapping([1,2,3], 7))     # [False, False, False]
    print(solution.subsequenceSumAfterCapping([1,2,3], 3))     # [True, True, True]
