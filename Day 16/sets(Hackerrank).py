def average(array):
    set_lst = list(set(array))
    num = len(set_lst)
    sum_lst = sum(set_lst)

    avg = sum_lst/num
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)