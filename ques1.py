from typing import List

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = 0
        for task in tasks:
            if res != 0 and task[0] + task[1] < res:
                res = task[0] + task[1]
            if res == 0:
                res = task[0] + task[1]
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.earliestTime([[1,6],[2,3]]))
    print(solution.earliestTime([[100,100],[100,100],[100,100]]))
    print(solution.earliestTime([[1,1],[1,2]]))