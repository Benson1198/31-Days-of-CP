def print_rangoli(size):
    s = size
    r = list(range(s))
    for i in r[:0:-1] + r:
        l = [chr(97+x) for x in r[:i:-1] + r[i:]]
        print('-'.join(l).center(4*s-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)