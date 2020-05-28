def grayToBinary(n):
    temp= n
    while temp !=0:
       temp= temp >> 1
       n= n ^ temp
   
    return n

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
