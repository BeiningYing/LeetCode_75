# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        skip_next = False
        max_flower = 0

        for i, flower in enumerate(flowerbed):
            # 如果种了花
            if flower == 1:
                skip_next = True
                continue
            # 如果没种花
            # 但前一个坑位种了花就跳过下一次遍历
            elif skip_next == True:
                skip_next = False
                continue
            # 下一个坑位未超过数组，下一个坑位也没有花
            elif i < len(flowerbed) - 1:
                if flower == 0 and flowerbed[i+1] == 0:
                    max_flower += 1
                    skip_next = True
            elif i == len(flowerbed) - 1:
                if flower == 0:
                    max_flower += 1                
            # 下一个坑位有花就什么事也不做
            else:
                continue
                
        
        return n <= max_flower
            
