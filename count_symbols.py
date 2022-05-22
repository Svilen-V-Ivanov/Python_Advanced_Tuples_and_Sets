line = input()

letter_dict = {}

for letter in line:
    if letter not in letter_dict:
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1

for word, number in sorted(letter_dict.items()):
    print(f"{word}: {number} time/s")
