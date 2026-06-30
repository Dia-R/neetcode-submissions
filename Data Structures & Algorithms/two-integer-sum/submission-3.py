class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsList = list(enumerate(nums))
        numsMap = {}
        for i,n in numsList:
            diff = target - n
            if diff in numsMap:
                return ([numsMap[diff], i])
            numsMap[n] = i
