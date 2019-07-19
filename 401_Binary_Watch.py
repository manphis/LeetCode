'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
'''


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num > 10:
            return []
        if num == 0:
            return ["0:00"]
        result = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    r = str(h) + ":{:02d}".format(m)
                    result.append(r)
                    
        return result