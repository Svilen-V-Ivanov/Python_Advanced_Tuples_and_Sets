usernames = int(input())
unique_names = set()
for _ in range(usernames):
    new_name = input()
    unique_names.add(new_name)

for name in unique_names:
    print(name)