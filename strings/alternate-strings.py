class Solution(object):
    def merge_alternatively(self, word_1, word_2):
        arr = []
        word_1_length = len(word_1)
        word_2_length = len(word_2)
        length = word_1_length if word_1_length > word_2_length else word_2_length
        i = 0
        while i < length:
            if i < word_1_length:
                arr.append(word_1[i:i+1])
            if i < word_2_length:
                arr.append(word_2[i:i+1])
            i = i + 1
        return ''.join(arr)
