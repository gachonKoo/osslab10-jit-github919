import sys

if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = int(input())  

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end="  ")

print()
