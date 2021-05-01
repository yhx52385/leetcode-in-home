# @Time    : 2021/5/1 10:43
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 001-two-sum.py
# @software: PyCharm
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueDict = {}
        for i in range(len(nums)):
            if(target - nums[i] not in valueDict.keys()):
                valueDict[nums[i]] = i
            else:
                return [i,valueDict[target-nums[i]]]
        return []
