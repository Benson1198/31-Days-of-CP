def biggerIsGreater(w):
    count,pivot,c=-1,0,1
    if len(set(w))==1:
        return "no answer"

    l=list(w)
    if l[-1]>l[-2]:
        l[-1],l[-2]=l[-2],l[-1]
        return "".join(l)
    
    for i in range(len(l)-1):
        if l[i]>=l[i+1]:
            c+=1
    if c==len(l):
        return "no answer"

    i = len(l) - 1
    while i > 0 and l[i - 1] >= l[i]:
        i -= 1
    
    if i <= 0:
        return "no answer" 
    j=len(l)-1
    while l[j]<=l[i-1]:
        j-=1

    l[j],l[i-1]=l[i-1],l[j]
    l[i:]=l[len(l)-1:i-1:-1]
    return "".join(l)

t = int(input())
for _ in range(t):
    s = input()
    print(biggerIsGreater(s))
    