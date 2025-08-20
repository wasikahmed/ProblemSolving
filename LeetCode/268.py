# Missing Number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum_of_array = sum(nums)
        sum_of_n_nums = n * (n + 1) // 2

        return sum_of_n_nums - sum_of_array

def main():
    solution = Solution()
    print(solution.missingNumber([3, 0, 1]))
    print(solution.missingNumber([0, 1]))
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))

if __name__ == "__main__":
    main()