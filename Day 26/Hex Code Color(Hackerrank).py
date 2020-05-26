import re
pattern0 = r'(\{(.*?)\})'
pattern1 = r'(#[0-9a-fA-F]+)'
pattern2 = r'#[0-9a-fA-F]{3}'
pattern3 = r'#[0-9a-fA-F]{6}'

N = int(input())

ss = ''
for _ in range(N):
    ss += input()


mm0 = re.findall(pattern0,ss)
    
for x in mm0:
    mm1 = re.findall(pattern1,x[1])
    for y in mm1:
        if re.match(pattern2,y) or re.match(pattern3,y):
            print(y)