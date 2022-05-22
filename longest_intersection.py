lines = int(input())
longest_set = set()
for _ in range(lines):
    order = input().split('-')
    one, two = (int(x) for x in order[0].split(','))
    three, four = (int(x) for x in order[1].split(','))

    first_set = set(range(one, two + 1))
    second_set = set(range(three, four + 1))

    intersected_set = first_set.intersection(second_set)
    if len(intersected_set) > len(longest_set):
        longest_set = intersected_set

print(f"Longest intersection is [{', '.join(str(x) for x in longest_set)}] with length {len(longest_set)}")
