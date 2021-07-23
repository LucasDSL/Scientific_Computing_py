file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except:
    print(f'File not found: {file_name}')
    quit()
letters_frequency = dict()
total_letters = 0
for line in file_handler: 
    line = line.rstrip()
    words = line.split() # Separate the line in words
    for word in words: # Read every word of the list of words in that line
        for letter in word: # Read every letter on the word
            number_ascii_letter = ord(letter.lower())
            letter = letter.lower()
            if (number_ascii_letter > 96 
            and number_ascii_letter < 123):
                letters_frequency[letter] = letters_frequency.get(letter, 0) + 1
                total_letters += 1
letters_freq_list = list()
for key, value in letters_frequency.items():
    letters_freq_list.append((round(value/total_letters, 3), key))
letters_freq_list = sorted(letters_freq_list, reverse=True)
print(letters_freq_list)