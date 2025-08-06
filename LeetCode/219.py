# Contains Duplicate ||

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table and i - hash_table[num] <= k:
                return True
            hash_table[num] = i
        return False


def main():
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


if __name__ == "__main__":
    main()
