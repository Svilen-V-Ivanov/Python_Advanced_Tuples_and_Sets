lines = int(input())
elements = set()
for _ in range(lines):
    line_of_elements = input().split(' ')

    for a in line_of_elements:
        elements.add(a)

for b in elements:
    print(b)
