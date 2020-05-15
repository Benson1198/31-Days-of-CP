class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        s=sum(A)
        l=[A[0]]
        for i in range(1,len(A)) :
            l.append(max(l[-1]+A[i],A[i]))
        max_sub=max(l)
        A=[-1*each for each in A]
        l=[A[0]]
        for i in range(1,len(A)) :
            l.append(max(l[-1]+A[i],A[i]))
        s=s+max(l)
        if s>max_sub and s!=0 :
            return s
        else :
            return max_sub