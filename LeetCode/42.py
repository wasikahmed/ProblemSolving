# Tapping Rain Water 

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            prefix_max = max(height[0:i+1])
            suffix_max = max(height[i:len(height)+1])
            res += min(prefix_max, suffix_max) - height[i]
        return res


def main():
    s = Solution()
    print(s.trap([0,2,0,3,1,0,1,3,2,1]))               # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))           # 6
    print(s.trap([4,2,0,3,2,5]))                       # 9


if __name__ == "__main__":
    main()