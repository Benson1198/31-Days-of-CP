n = int(input())

inputs = {}

for _n in range(n):
    time = input()
    if(time in inputs):
        inputs[time]+=1
    else:
        inputs[time]=1

cash = 0
for time in inputs:
    if(inputs[time]>cash):
        cash = inputs[time]
print(cash)