from collections import defaultdict

class Taxi:
    def solve(self,n,students):
        d = defaultdict(int)
        for i in students:
            d[i] +=1
        
        taxiCount = 0 
        
        taxiCount+= d[4]+d[3]
        
        d[1]-=d[3]
        taxiCount+= (d[2]/2)
        if(d[2]%2>0):
            taxiCount+=1
            d[1]-=2
        if(d[1]>0):
            taxiCount+=(d[1]/4)
            if(d[1]%4>0):
                taxiCount+=1
        
        return taxiCount 
                

students = list()
n = int(input())
students = [int(y) for y in input().split()]
    
t = Taxi()
ans = t.solve(n,students)
print(int(ans))