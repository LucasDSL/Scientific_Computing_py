file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except:
    print(f'File not found: {file_name}')
    quit()
all_words = []
for line in file_handler:
    line = line.rstrip()
    words_at_line = line.split()
    for word in words_at_line: 
        if word not in all_words: all_words.append(word)
all_words.sort()
print(all_words)