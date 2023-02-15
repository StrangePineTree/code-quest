'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())
num1 = 0
num2 = 0
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [val for val in line.split(SEPARATOR)]

    num1 = int(args[0]) + int(args[1])
    num2 = int(args[0]) * int(args[1])

    print(num1, num2)
    