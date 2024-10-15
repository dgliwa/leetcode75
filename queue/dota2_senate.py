# https://leetcode.com/problems/dota2-senate/
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = len(senate)
        r = deque()
        d = deque()

        for i in range(count):
            if senate[i] == "D":
                d.append(i)
            else:
                r.append(i)

        while r and d:
            r_val = r.popleft()
            d_val = d.popleft()
            if r_val < d_val:
                r.append(r_val + count)
            else:
                d.append(d_val + count)

            count += 1

        return "Dire" if d else "Radiant"
