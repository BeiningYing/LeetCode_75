# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [inf] * 3
        for i in range(n):
            t = nums[i]
            if f[2] < t:
                return True
            elif f[1] < t < f[2]:
                f[2] = t
            elif f[1] > t:
                f[1] = t
        return False