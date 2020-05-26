eng=int(input())      
eng_roll=list(map(int,input().split()))[:eng]    
set1=set(eng_roll)    
fre=int(input())    
fre_roll=list(map(int,input().split()))[:fre]    
set2=set(fre_roll)    
length=set1.union(set2)    
print(len(length)) 