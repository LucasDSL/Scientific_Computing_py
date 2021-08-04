file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except: 
    print('File could not be found.')
    quit()
count = 0 
for line in file_handler: 
    line = line.rstrip()
    count += 1
    if line.startswith('a'):
        continue 
    print(line)
print(f'There are a total of {count} lines in this file.')