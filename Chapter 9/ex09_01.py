file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except: 
    print('File could not be found.')
    quit()
count = 0
words = dict()
for line in file_handler:
    line = line.rstrip()
    words_at_line = line.split()
    for word in words_at_line: 
        if word in words: break
        words[word] = count 
        count += 1

print (words)