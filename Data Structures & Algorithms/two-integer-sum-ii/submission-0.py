from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1
        
        while leftPointer < rightPointer:
            currentSum = numbers[leftPointer] + numbers[rightPointer]
            
            if currentSum == target:

                return [leftPointer + 1, rightPointer + 1]
            elif currentSum < target:
                leftPointer += 1  
            else:
                rightPointer -= 1  
                
