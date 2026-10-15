class Solution:
    def productExceptSelf(self, nums):
        p = len(nums)
        output = [1] * p

        left = 1
        for i in range(p):
            output[i] = left
            left = left * nums[i]
        right = 1
        for j in range(p - 1, -1, -1):
            output[j] = output[j] * right
            right = right * nums[j]
        return output
