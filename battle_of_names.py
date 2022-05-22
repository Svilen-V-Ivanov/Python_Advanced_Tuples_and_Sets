lines = int(input())
odd_set = set()
even_set = set()
result = set()
for line in range(1, lines + 1):
    current_name = input()
    sum_name = sum(ord(x) for x in current_name) // line

    if sum_name % 2 == 0:
        even_set.add(sum_name)
    else:
        odd_set.add(sum_name)

if sum(odd_set) == sum(even_set):
    result = even_set.union(odd_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(', '.join(str(x) for x in result))
