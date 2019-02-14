'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
'''

class Solution:
    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
        if ransomNote == None or magazine == None:
            return False
        
        noteMap = self.getMap(ransomNote)
        magazineMap = self.getMap(magazine)
        
        for key, value in noteMap.items():
            if key not in magazineMap:
                return False
            else:
                if magazineMap[key] < value:
                    return False
        return True
        
        
    def getMap(self, str):
        map = dict()
        for i in range(len(str)):
            if str[i] in map:
                map[str[i]] += 1
            else:
                map[str[i]] = 1
        return map