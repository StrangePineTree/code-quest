import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]
    if args[0] != args[1]:
        print(args[0] + args[1])
    else:
        print((args[1] + args[0]) * 2)
