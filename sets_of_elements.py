a, b = [int(x) for x in input().split(' ')]
set_a = set()
set_b = set()

for num in range(a):
    set_a.add(input())

for nums in range(b):
    set_b.add(input())

new_set = set_a.intersection(set_b)

for c in new_set:
    print(c)
