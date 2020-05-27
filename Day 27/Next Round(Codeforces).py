class NextRound:
    def sovle(self,n,k,numList):
        result = 0
        for i in numList:
            if(i>0 and i>=numList[k-1]):
                result+=1
        return result
        
        
        

numList = list()
n,k = [int(y) for y in input().split()]
numList = [int(y) for y in input().split()]
nr = NextRound()
print(nr.sovle(n,k,numList))