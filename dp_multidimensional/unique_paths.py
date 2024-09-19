# https://leetcode.com/problems/unique-paths
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        paths = {(0,0): 1}

        for i in range(m):
            for j in range(n):
                if (i+1,j) not in paths:
                    paths[(i+1,j)] = paths[(i,j)]
                else:
                    paths[(i+1,j)] = paths[(i+1,j)] + paths[(i,j)]
                if (i,j+1) not in paths:
                    paths[(i,j+1)] = paths[(i,j)]
                else:
                    paths[(i,j+1)] = paths[(i,j+1)] + paths[(i,j)]

        return paths[(m-1,n-1)]

        
    
