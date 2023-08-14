from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        prefix = ""

        for i in range(min(len(s) for s in strs)):
            char = strs[0][i]

            for s in strs[1:]:
                if s[i] != char:
                    return prefix

            prefix += char

        return prefix
