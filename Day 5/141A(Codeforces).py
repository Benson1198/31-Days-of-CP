s1 = input()
len1 = len(s1)
s1_lst_set = list(s1)

s2 = input()
len2 = len(s2)
s2_lst_set = list(s2)

s3 = input()
len3 = len(s3)
s3_lst_set = list(s3)
s3_lst_set.sort()

sum_lst = s1_lst_set + s2_lst_set
# sum_lst = list(set(sum_lst))
sum_lst.sort()

if ((len1 + len2) == len3) and (sum_lst == s3_lst_set):
    print('YES')
else:
    print('NO')


