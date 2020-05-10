class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N == 1:
            return 1
        
        trustedBy = collections.defaultdict(list)
        trusts = collections.defaultdict(list)
        for t in trust:
            trustedBy[t[1]].append(t[0])
            trusts[t[0]].append(t[1])
            
        judge = -1
        
        for person,trustedByList in trustedBy.items():
            everybodyTrusts = len(trustedByList) == N - 1
            if everybodyTrusts:
                trustsNoone = len(trusts[person]) == 0
                if trustsNoone:
                    judge = person
                else:
                    break
        
        return judge