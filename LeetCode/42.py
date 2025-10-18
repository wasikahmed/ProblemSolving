# Tapping Rain Water 

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n^2) solution --- because of checking max inside the loop
        # res = 0
        # for i in range(len(height)): # O(n)
        #     prefix_max = max(height[0:i+1]) # O(n)
        #     suffix_max = max(height[i:len(height)+1]) # O(n)
        #     res += min(prefix_max, suffix_max) - height[i] # O(1)
        # return res
        # complexity = O(n) * {O(n) + O(n) + O(1)} = 2*O(n^2) -> O(n^2)


        ## O(n) solution
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        # O(n)
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        # O(n)
        right_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # O(n)
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
        # complexity = O(n) + O(n) + O(n) = 3*O(n) -> O(n)

def main():
    s = Solution()
    print(s.trap([0,2,0,3,1,0,1,3,2,1]))               # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))           # 6
    print(s.trap([4,2,0,3,2,5]))                       # 9


if __name__ == "__main__":
    main()