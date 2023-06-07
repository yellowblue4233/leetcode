# 448. 找到所有数组中消失的数字
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/
# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

# 示例 1：
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]

# 示例 2：
# 输入：nums = [1,1]
# 输出：[2]

## 思路1
## 先将所有候选数值放进answer里，之后再进行排除，
## 此时，answer中的索引与数值相关，index = value - 1， 
## 在answer中，将在nums中出现过的数值赋为0，
## 最后筛选出没有变为0的数值即为最终答案
## 执行用时: 80 ms 内存消耗: 22.8 MB

from typing import List

class Solution:    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = list(range(1, len(nums) + 1))
        for i in range(len(nums)):
            answer[nums[i] - 1] = 0 
        answer = [x for x in answer if x != 0]
        return answer

## 思路2
## 原地Hashmap，用负号作为标记，使用求绝对值去除标记影响，
## 也可以加上n作为标记，使用求余去除标记影响，
## 最后留下的没有标记的数值，其索引+1就是最终答案
## 执行用时: 104 ms 内存消耗: 23.1 MB
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = - nums[abs(nums[i]) - 1]
        for i in range(len(nums)):
            if nums[i] > 0:
                answer.append(i + 1)
        return answer