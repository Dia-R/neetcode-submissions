class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        i = 0
        j = i+1
        while (j<len(nums)):
            if nums[i]==nums[j]:
                return True
            else:
                i+=1
                j+=1
        return False
         