class Solution:
    def longestConsecutive(self, nums):
        sum = set(nums)
        long = 0

        for num in sum:
            if num -1 not in sum:
                count = 1

                while num + count in sum:
                     count += 1
                long = max(long, count)
        return long


        