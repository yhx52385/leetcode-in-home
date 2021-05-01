# @Time    : 2021/5/1 10:22
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 242-valid-anagram.py
# @software: PyCharm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicStr = {}
        for ch in s:
            if(ch not in dicStr.keys()):
                dicStr[ch] = 1
            else:
                dicStr[ch] = dicStr[ch] +1
        for ch in t:
            if(ch in  dicStr.keys()):
                dicStr[ch] = dicStr[ch]-1
                if(dicStr[ch] == 0):
                    dicStr.pop(ch)
            else:
                return False
        if(len(dicStr.keys()) == 0):
            return True
        return False
