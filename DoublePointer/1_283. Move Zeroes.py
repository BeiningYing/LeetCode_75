# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return 0
        j = 0

        # # 将非0数挪到前面
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[j] = nums[i]
        #         j += 1
        # # 在j之后全部补0
        # for i in range(j, len(nums)):
        #     nums[i] = 0
        
        # 左右交换
        for i in range(len(nums)):
            # 如果i的数不为0
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
    
            