'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

def fib(num:int) -> int:
    output = 1
    num1 = 0
    num2 = 1
    if num <2:
        return 0
    elif num <= 3:
        return 1
    for _ in range(num-2):
        output = num1 + num2
        num1 = num2
        num2 = output
    return output

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    print(line, "=", fib(line))
