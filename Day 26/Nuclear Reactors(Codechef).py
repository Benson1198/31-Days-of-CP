a,n,k = map(int,input().split(' '))
    
li = [0]*k 
n+=1
for i in range(k):
        
    li[i] = a%n
    a  = int(a//n)
        
    if a < 1:
        break
    
print(*li)