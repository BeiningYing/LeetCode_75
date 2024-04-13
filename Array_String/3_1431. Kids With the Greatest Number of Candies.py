# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n = len(candies)
        # ans = [False] * n
        # maxc = max(candies)
        # for i, candie in enumerate(candies):
        #     if (candie + extraCandies) >= maxc:
        #         ans[i] = True
        # ans = [True for i, candie in enumerate(candies) if (candie + extraCandies) >= maxc]
        # return ans
        maxc = max(candies)
        return [candie + extraCandies >= maxc for candie in candies]