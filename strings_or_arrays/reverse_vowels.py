# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def __init__(self):
        self.vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if arr[i] in self.vowels and arr[j] in self.vowels:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                j -= 1
                i += 1
            elif arr[i] in self.vowels:
                j -= 1
            elif arr[j] in self.vowels:
                i += 1
            else:
                j -= 1
                i += 1
        return ''.join(arr)
