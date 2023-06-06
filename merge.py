# 88. 合并两个有序数组
# https://leetcode.cn/problems/merge-sorted-array/
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
# 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

# 示例 1：
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

# 示例 2：
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。

# 示例 3：
# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

## 思路
## 1. 倒序循环，从大到小排列，从后往前放置（比合并后排序要好）
## 2. 需要三个指针，用于存放的 k ，用于比较的 i 和 j
## 3. 考虑三种情况：(示例3)m=0，(示例2)n=0 和 (示例1)m!=0 and n!=0
##    因为是没有返回值，直接修改nums1，所以情况2直接返回nums1，不需要额外操作，
##    而情况1需要将nums2的值赋给nums1，情况3是通常情况
## 4. 当其中一个列表没有数值可以比较时，即 i < 0 or j < 0 时，之后不需要比较，
##    直接跳出用于比较的循环，按顺序赋值给nums1比较快(48ms -> 40 ms) 

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for k in range(m + n):
                nums1[k] = nums2[k]
        elif n != 0 and m != 0:
            i = m - 1
            j = n - 1
            for k in range(m + n - 1, -1, -1):
                if j < 0 or i < 0:
                    break
                elif nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i = i - 1
                else: 
                    nums1[k] = nums2[j]
                    j = j - 1
            if i < 0:
                for k in range(j + 1):
                    nums1[k] = nums2[k]
            elif j < 0:
                for k in range(i + 1):
                    nums1[k] = nums1[k]
