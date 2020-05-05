s = input()

s_lst_set = set(list(s))
if len(s_lst_set)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')