import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]
    if args[0] >= 70:
        print("PASS")
    else:
        print('FAIL')
