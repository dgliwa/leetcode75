# https://leetcode.com/problems/smallest-number-in-infinite-set/

import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.current_smallest = 1
        self.added_ints = set()
        self.min_added = []

    def popSmallest(self) -> int:
        if not self.min_added or self.current_smallest < self.min_added[0]:
            self.current_smallest += 1
            return self.current_smallest - 1
        else:
            smallest = heapq.heappop(self.min_added)
            self.added_ints.remove(smallest)
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current_smallest and num not in self.added_ints:
            heapq.heappush(self.min_added, num)
            self.added_ints.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
