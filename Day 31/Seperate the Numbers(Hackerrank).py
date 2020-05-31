def find(st):
    for i in range(len(st)//2):
        dig = int(st[:i+1], 10)
        arr = str(dig)
        m = arr
        while len(arr) < len(st):
            dig = dig + 1
            arr += str(dig)
        if len(st) is len(arr):
            for i in range(len(st)):
                if arr[i] != st[i]:
                    break
            else:
                return ('YES', m)
    return ('NO', '')
        
test_cases = int(input())
for _ in range(test_cases):
    st = input()
    k = find(st)
    for i in k:
        print(i, end = " ")
    print()