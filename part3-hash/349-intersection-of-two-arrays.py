# @Time    : 2021/5/1 10:28
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 349-intersection-of-two-arrays.py
# @software: PyCharm
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set()
        resList = set()
        for item in nums1:
            numSet.add(item)
        for item in nums2:
            if(item in numSet):
                resList.add(item)
        return list(resList)
