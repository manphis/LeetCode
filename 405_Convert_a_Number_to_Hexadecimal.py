'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
'''

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        self.hexStr = ['0', '1','2', '3','4', '5', '6','7', '8','9', 'a','b', 'c','d', 'e','f']
        
        if num >= 0:
            output = self.getHex(num)
        else:
            output = self.getHex(self.getPositive(num))
            
        return output
    
    def getHex(self, num):
      print('num =', num)
      output = ''
      n = 0
      for i in range(32):
        if 16 ** i > num:
          n = i-1
          break
      print('n =', n)
      if n == 0:
        return self.hexStr[num]
        
      while n >= 0:
        s = int(num/(16**n))
        print(s)
        output += self.hexStr[s]
        num -= s*(16**n)
        n -=1
      
      return output
        
    
    def getPositive(self, num):
        return 2 ** 32 + num