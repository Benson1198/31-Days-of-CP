def main():
    n1, n2, n3 = map(int, input().split())
    n1_list = {}
    n2_list = {}
    n3_list = {}
    voter_list = []

    n1_list = {int(input()) for n in range(n1)}
    n2_list = {int(input()) for n in range(n2)}
    n3_list = {int(input()) for n in range(n3)}

    voter_list = sorted(list((n1_list & n2_list) | (n1_list & n3_list) | (n2_list & n3_list)))

    print(len(voter_list))
    for idx in range(len(voter_list)):
        print(voter_list[idx])
 
 
if __name__ == '__main__':
    main()