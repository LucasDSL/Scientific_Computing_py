word = "pneumoultramicroscopicossilicovulcanoconiotico"
letters_frequency = dict()
for letter in word:
    letters_frequency[letter] = letters_frequency.get(letter, 0) + 1
print(letters_frequency)