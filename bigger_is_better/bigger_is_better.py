'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())
length = 0
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]

    args.sort()
    print(args[-1])
