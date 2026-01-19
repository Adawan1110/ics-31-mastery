# Last updated: 1/19/2026, 2:32:36 PM
1# class Solution(object):
2#     def twoSum(nums, target):
3#         for x in range(len(nums)):
4#             for y in range(1, len(nums)):
5#                 if nums[x] + nums[y] == target:
6#                     z = (nums[x], nums[y])
7#                     print(z)
8#                 else:
9#                     print("Error")
10
11class Solution(object):
12    def twoSum(self, nums, target):
13        val_idx = {} # key is val, val is index
14
15        for i, num in enumerate(nums):
16            if target - num in val_idx:
17                return (i, val_idx[target - num])
18            val_idx[num] = i
19
20            
21
22
23        