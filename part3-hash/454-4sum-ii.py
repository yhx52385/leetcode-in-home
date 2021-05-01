# @Time    : 2021/5/1 11:40
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 454-4sum-ii.py
# @software: PyCharm
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        numDict12 = {}
        numDict34 = {}
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                value = nums1[i] + nums2[j]
                if(value not in numDict12.keys()):
                    numDict12[value] = 1
                else:
                    numDict12[value] +=1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                value = nums3[i] + nums4[j]
                if (value not in numDict34.keys()):
                    numDict34[value] = 1
                else:
                    numDict34[value] += 1
        for key in numDict12.keys():
            if(-key in numDict34.keys()):
                resNum = numDict12[key]*numDict34[-key]
                res = res +resNum
                # for item1 in numDict12[key]:
                #     for item2 in numDict34[-key]:
                #         res = (item1[0],item1[1],item2[0],item2[1])
                #         resList.append(res)
        return res

    def fourSumCount_old(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        numDict12 = {}
        numDict34 = {}
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                value = nums1[i] + nums2[j]
                if (value not in numDict12.keys()):
                    numDict12[value] = [(i, j)]
                else:
                    numDict12[value].append((i, j))

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                value = nums3[i] + nums4[j]
                if (value not in numDict34.keys()):
                    numDict34[value] = [(i, j)]
                else:
                    numDict34[value].append((i, j))
        for key in numDict12.keys():
            if (-key in numDict34.keys()):
                resNum = len(numDict12[key]) * len(numDict34[-key])
                res = res + resNum
                # for item1 in numDict12[key]:
                #     for item2 in numDict34[-key]:
                #         res = (item1[0],item1[1],item2[0],item2[1])
                #         resList.append(res)
        return res

