file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except:
    print(f'File not found: {file_name}')
    quit()
hours_count = dict()
for line in file_handler: 
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 5: continue
    hours = words[5].split(':')[0]
    hours_count[hours] = hours_count.get(hours, 0) + 1
hours_count = sorted(hours_count.items())
for key, value in hours_count:
    print(key, value)