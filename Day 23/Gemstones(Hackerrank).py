rocks = []
for i in range(int(input())):
    rocks.append(set(input()))
gems = set.intersection(*rocks)
print(len(gems))