#User function Template for python3


##Complete this function
def isPowerofTwo(n):
    if n==0:
        return False
    elif (n & (n-1)):
        return False
    else:
        return True

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()