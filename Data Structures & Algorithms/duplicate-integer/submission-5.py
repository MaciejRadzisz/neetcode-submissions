class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        while(True):
            if len(nums) == 1 or len(nums) == 0:
                return False
            i = nums[0]
            nums.remove(i)
            if i == nums[0]:
                return True
        