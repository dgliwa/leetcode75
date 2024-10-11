# https://leetcode.com/problems/decode-string/
from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                current_string = ""

                while stack[-1] != '[':
                    current_string = current_string + stack.pop()

                stack.pop()
                digit = ""
                while stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append(int(digit) * current_string)

        return ''.join(stack)
