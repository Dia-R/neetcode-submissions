class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_map = set()
        for n in nums:
            if n not in nums_map:
                nums_map.add(n)

            else:
                return True
            
        return False

        
         