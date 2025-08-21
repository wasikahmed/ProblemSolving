# Two Sum || - Input Array Is Sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, value in enumerate(numbers):
            x = target - value
            if x in hash_map:
                return [hash_map.get(x) + 1, index + 1]
            hash_map[value] = index