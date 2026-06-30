class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        prefixArray=[1]*len(nums)
        postfixArray=[1]*len(nums)

        for i in range(len(nums)):
            prefixArray[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)):
            postfixArray[len(nums)-(i+1)] = postfix
            postfix *= nums[len(nums)-(i+1)]

        output =[]
        for i in range(len(nums)):
            output.append(prefixArray[i]*postfixArray[(i)])

        return output

        