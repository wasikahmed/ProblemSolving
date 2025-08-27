# Permutations

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutations(result, arr, idx):

            # Base case
            if idx == len(arr):
                result.append(arr[:])
                return
            
            # Permutations made by swapping each element
            for i in range(idx, len(arr)):
                arr[idx], arr[i] = arr[i], arr[idx]
                permutations(result, arr, idx + 1)
                arr[idx], arr[i] = arr[i], arr[idx]
        
        permutations(res, nums, 0)
        return res

def main():
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(solution.permute([0, 1]))
    print(solution.permute([1]))


if __name__ == "__main__":
    main()