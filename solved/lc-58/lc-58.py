class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()

        i = -1

        while (i*-1) < len(s):

            if s[i] == ' ':
                return (i+1) * -1

            i -= 1

        return (i) * -1
