# https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution:
    def __init__(self):
        self.digit_lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        combinations = []
        self.build_combination(digits, 0, "", combinations)
        return combinations
        

    
    def build_combination(self, digits: str, index: int, current_combination: str, combinations: List[str]) -> List[str]:
        if len(digits) == index:
            combinations.append(current_combination)
            return
        
        digit = digits[index]
        for c in self.digit_lookup[digit]:
            self.build_combination(digits, index + 1, current_combination + c, combinations)

