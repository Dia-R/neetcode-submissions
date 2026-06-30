from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        finalCount = 0
        currentCount = 0
        numSet = set(nums)
        
        start = min(numSet)
        end = max(numSet)
        numList = list(range(start, end + 1))

        for i in range(len(numList)):
            if numList[i] in numSet:
                currentCount += 1
            else:
                finalCount = max(finalCount, currentCount)
                currentCount = 0
        
        finalCount = max(finalCount, currentCount)
        
        return finalCount
