from collections import deque

numbers = [int(x) for x in input().split(' ')]
goal = int(input())

redundant_set = deque(numbers)
count = 0
dict = {}

for a in numbers:
    redundant_set.popleft()
    for b in redundant_set:
        count += 1
        if a + b == goal:
            print(f'{a} + {b} = {goal}')
            dict[a] = b

print(f'Iterations done: {count}')
for first, second in dict.items():
    print(f'({first}, {second})')
