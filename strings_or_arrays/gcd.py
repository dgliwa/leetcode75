# https://leetcode.com/problems/greatest-common-divisor-of-strings
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        str1_len = len(str1)
        str2_len = len(str2)

        if str1_len == str2_len:
            return ""
        gcd_len = math.gcd(str1_len, str2_len)

        possible_gcd = str1[-gcd_len:]

        for i in range(0, str1_len, gcd_len):
            str1_segment = str1[i:i+gcd_len]
            if str1_segment != possible_gcd:
                return ""
        for i in range(0, str2_len, gcd_len):
            str2_segment = str2[i:i+gcd_len]
            if str2_segment != possible_gcd:
                return ""
        return possible_gcd
