# https://leetcode.com/problems/number-of-recent-calls
class RecentCounter(object):

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        window = t - 3000
        while self.pings and self.pings[0] < window:
            self.pings.pop(0)
        self.pings.append(t)
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
