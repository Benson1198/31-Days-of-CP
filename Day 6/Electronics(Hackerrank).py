import os
import sys
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    key_len = len(keyboards)
    drive_len = len(drives)
    max_spend = 0
    for i in range(key_len):
        for j in range(drive_len):
            if (keyboards[i] + drives[j]) > max_spend and (keyboards[i] + drives[j]) <= b:
                max_spend = keyboards[i] + drives[j]
    if max_spend == 0:
        return -1
    else:
        return max_spend

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
