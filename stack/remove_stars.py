class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = []
        chars = list(s)
        skip_count = 0
        while len(chars) > 0:
            c = chars.pop()
            if c == '*':
                skip_count = skip_count + 1
            else:
                if skip_count > 0:
                    skip_count = skip_count - 1
                else:
                    answer.append(c)
        return ''.join(reversed(answer))
            
            
            
