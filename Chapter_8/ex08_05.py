file_name = input('Enter file name: ')
try:
    file_handler = open(file_name)
except:
    print(f'File not found: {file_name}')
    quit()
number_of_lines_starting_with_from = 0
for line in file_handler: 
    line = line.rstrip()
    if not line.startswith('From'): continue 
    words = line.split()
    print(words[1])
    number_of_lines_starting_with_from += 1
print(f'There were {number_of_lines_starting_with_from} lines in the file wiith From as the first word.')
