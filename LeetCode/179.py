from typing import List

class Solution:
    def largestNumber(self, nums: List[int]):
        nums.sort()
        return nums


def main():
    solution = Solution()
    print(solution.largestNumber([10,2]))
    print(solution.largestNumber([3,30,34,5,9]))


if __name__ == "__main__":
    main()