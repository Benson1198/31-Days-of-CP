
def SubsequenceLength(s):
    p={}
    l=len(s)
    srt=0
    v=0
    for i in range(l):
        if s[i] in p:
            srt=max(srt,p[s[i]]+1)
        p[s[i]]=i;
        v=max(v,i-srt+1)
    return v