file_name = input('Enter a file name: ')

try:
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()

for line in file_handler:
    line = line.rstrip().upper() # Remove the blank space at the end of the line and set the whole line to upper case 
    print(line)