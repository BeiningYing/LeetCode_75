# You are given an integer num. You will apply the following steps exactly two times:

# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# The new integer cannot have any leading zeros, also the new integer cannot be 0.
# Let a and b be the results of applying the operations to num the first and second times, respectively.

# Return the max difference between a and b.

class Solution:
    def maxDiff(self, num: int) -> int:
        min_num, max_num = str(num), str(num)

        # MAX: Highest position
        for d in max_num:
            if d != "9":
                max_num = max_num.replace(d,"9")
                break
        
        # MIN
        for i, d in enumerate(min_num):
            if i == 0:
                if d != "1":
                    min_num = min_num.replace(d, "1")
                    break
            else:
                if d != "0" and d != "1":
                    min_num = min_num.replace(d, "0")
                    break
        
        # Output
        return int(max_num) - int(min_num)