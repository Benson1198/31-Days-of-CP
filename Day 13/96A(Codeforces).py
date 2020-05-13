s = input()

def seven_count(s):
    count = 0

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
            if count == 6:
                return 'YES'
        else:
            count = 0
    return 'NO'

print(seven_count(s))
