from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        uniques = set()

        for email in emails:

            l, d = email.split('@')
            l = l.split('+')[0].replace(".", "")

            uniques.add(l + "@" + d)

        return len(uniques)
