class Solution :
    def twoSum(self, nums,target):
       seen = {}
       for i, num in enumerate(nums):
           needed = target - num
           if needed in seen:
              return [seen[needed], i]
           seen[num] = i

       return[]
solution = Solution()
print(solution.twoSum([3,4,5,6],7))