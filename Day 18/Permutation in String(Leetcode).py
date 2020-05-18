class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        s1_arr = [0]*26
        for i in list(s1):
            ind = alpha.find('i')
            s1_arr[ind] += 1

        for x in range(len(s2) - len(s1) + 1):
            temp_arr = [0]*26
            temp_s2 = s2[x:x+3]
            for i in list(temp_s2):
                ind = alpha.find('i')
                temp_arr[ind] += 1
            if temp_arr == s1_arr:
                return True
        return False

        