file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except:
    print(f'File not found: {file_name}')
    quit()
messages_count = dict()
for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    email = words[1]
    messages_count[email] = messages_count.get(email, 0) + 1

# Creating a list where the value comes first
list_tuples = list()
for key, value in messages_count.items():
    list_tuples.append((value, key))
list_tuples = sorted(list_tuples, reverse=True)
print(list_tuples[0][1], list_tuples[0][0])