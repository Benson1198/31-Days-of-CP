n = int(input())
def viral_advertising(n):
    if(1<=n<=50):
        i=1
        k=5
        cumu=0
        while(i<=n):
            shared=k
            liked=shared//2
            cumu=liked+cumu
            k=liked*3
            i+=1
        return cumu

print(viral_advertising(n))