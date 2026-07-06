class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        freqCount = [[] for i in range(len(nums)+1)]
  
        for i in range(len(nums)):
            if nums[i] in frequencyMap:
                frequencyMap[nums[i]] = 1 + frequencyMap.get(nums[i])
            else:
                frequencyMap[nums[i]] = 1
        print(frequencyMap.items())
        for n,c in frequencyMap.items():
            freqCount[c].append(n)
        print(freqCount)

        res = []
        

        for numbers in freqCount[::-1]:
            if numbers != []:
                for i in range(len(numbers)):
                    res.append(numbers[i])
            if len(res) == k:
                return(res)

                
            


        
