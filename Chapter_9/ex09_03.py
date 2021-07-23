file_name = input('Enter file name: ')
try:
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()
emails = dict()
for line in file_handler: 
    line = line.rstrip()
    if not line.startswith('From'): continue 
    words = line.split() 
    emails[words[1]] = emails.get(words[1], 0) + 1   
print(emails)
        