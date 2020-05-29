def printNos(N):
    if N == 0:
        return
    else:
        printNos(N-1)
        print (N,end=" ")

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()