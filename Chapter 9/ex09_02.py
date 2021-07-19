file_name = input('Enter file name: ')
try:
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()
days = dict()
for line in file_handler: 
    line = line.rstrip()
    if not line.startswith('From'): continue 
    words = line.split() 
    if len(words) < 3: continue
    day_in_now_word = words[2]
    days[day_in_now_word] = days.get(day_in_now_word, 0) + 1
print(days)
        