from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        output = []

        for r in range(numRows):
            row = [1] * (r + 1)
            for i in range(1, r):
                row[i] = output[r - 1][i - 1] + output[r - 1][i]
            output.append(row)

        return output
