'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''

class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ls = list(s)
        size = len(s)
        j = size - 1
        for i in range(size):
            if i == j:
                break
            if ls[i] in vowels:
                while j > i:
                    if ls[j] in vowels:
                        tmp = ls[i]
                        ls[i] = ls[j]
                        ls[j] = tmp
                        j -= 1
                        break
                    j -= 1
        str1 = ''.join(ls)
        return str1