number_names = int(input())
unique_names = set()

for _ in range(number_names):
    unique_names.add(input())

[print(name) for name in unique_names]

