# @Time    : 2021/5/1 10:32
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 202-happy-number.py
# @software: PyCharm
class Solution:
    def isHappy(self, n: int) -> bool:
        sumSet = set()
        while(n!=1):
            if(n in sumSet):
                return False
            else:
                sumSet.add(n)
                n = self.cycleOnce(n)
        return True
    def cycleOnce(self,n):
        sum = 0
        value = 0
        while(n):
            value = pow(n%10,2)
            n = n//10
            sum = sum + value
        return sum

n = 2
s = Solution()
print(s.isHappy(n))