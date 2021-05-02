# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    line = line.strip()
    num = any(char.isdigit() for char in line)
    if (num == False):
        even, odd = line[::2], line[1::2]
        print(even + " " + odd)
