import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        d = collections.deque()
        maxes = []

        for i, n in enumerate(nums):

            while d and nums[d[-1]] < n:

                d.pop()

            d.append(i)

            if d[0] == i - k:

                d.popleft()

            if i >= k-1:

                maxes.append(nums[d[0]])

        return maxes
