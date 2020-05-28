def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count

def countBitsFlip(a,b):
    c = a^b
    
    return countSetBits(c)
import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        print(countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
