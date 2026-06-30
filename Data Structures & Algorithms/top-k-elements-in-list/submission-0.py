class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        output = []
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        for j in range(k):
            X = max(hashMap.values())
            for key, value in hashMap.items():
                if X == value:
                    output.append(key)
                    hashMap.pop(key)
                    break
              
        return output