from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rm = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], rm = rm, max(rm, arr[i])

        return arr
