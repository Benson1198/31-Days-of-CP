m = input()
m_set = set(input().split())
n = input()
n_set = set(input().split())

sym_dif = set(m_set.union(n_set) - m_set.intersection(n_set))

x = []
for i in sym_dif:
    x.append(int(i))
x.sort()

for i in x:
    print(i)