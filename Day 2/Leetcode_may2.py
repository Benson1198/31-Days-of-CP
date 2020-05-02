# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_arr = list(J)
        s_arr = list(S)
        
        no_of_jewel = 0
        
        for i in range(len(s_arr)):
            if s_arr[i] in j_arr:
                no_of_jewel += 1
        return no_of_jewel