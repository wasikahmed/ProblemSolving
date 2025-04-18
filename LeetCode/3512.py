# Minimum Operations to Make Array Sum Divisible by K

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


def main():
    s = Solution()
    print(s.minOperations([3, 9, 7], 5))
    print(s.minOperations([4, 1, 3], 4))


if __name__ == "__main__":
    main()
