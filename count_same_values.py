numbers_list = (float(x) for x in input().split(' '))

occurrences_dict = {}

for number in numbers_list:
    if number not in occurrences_dict:
        occurrences_dict[number] = 0

    occurrences_dict[number] += 1

for number, counts in occurrences_dict.items():
    print(f'{number:.1f} - {counts} times')
