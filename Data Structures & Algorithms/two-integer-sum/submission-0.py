class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            x = target-nums[i]
            if x in hash_map and i != hash_map.get(x):
                if i < hash_map.get(x):
                    return [i, hash_map.get(x)]
                if i > hash_map.get(x):
                    return [hash_map.get(x), i]
            
        