class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        arr = []
        for i in range(len(nums)):
            b = nums[i]
            a = target - b
            if a in pair.keys():
                arr.append(pair[a])
                arr.append(i)
                return arr
            else:
                pair[b] = i