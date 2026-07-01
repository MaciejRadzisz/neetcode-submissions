class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i in range(len(nums)):
            b = nums[i]
            a = target - b
            if a in pair.keys():
                return [pair[a], i]
            else:
                pair[b] = i