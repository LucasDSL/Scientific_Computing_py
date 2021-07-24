# grep 
import re 
file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()
rex = input('Enter regular expression: ')
lines_equal_regex = 0
for line in file_handler:
    line = line.rstrip()
    equal = re.findall(rex, line)
    if len(equal) != 0: 
        lines_equal_regex += 1
print(f'{file_name} had lines {lines_equal_regex} that are equal {rex}') 
