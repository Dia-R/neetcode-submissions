class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countNums = {}
        for i in range(len(nums)):
            if nums[i] not in countNums:
                countNums[nums[i]] = [i]
            else:
                countNums[nums[i]].append(i)  

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in countNums:
                continue
            if complement == nums[i]:
                if len(countNums[nums[i]]) >= 2:
                    return countNums[nums[i]][:2]
            else:
                return [countNums[nums[i]][0], countNums[complement][0]]