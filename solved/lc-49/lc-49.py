from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = {}

        for s in strs:
            a = ''.join(sorted(s))
            if a in ret:
                ret[a].append(s)
            else:
                ret[a] = [s]

        return list(ret.values())
