file_name = input('Enter file name: ')
try:
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()
domains = dict()
for line in file_handler: 
    line = line.rstrip()
    if not line.startswith('From'): continue 
    words = line.split() 
    domain = words[1].split('@')[1] # Get the domain after split the word/email
    domains[domain] = domains.get(domain, 0) + 1   
print(domains)
        