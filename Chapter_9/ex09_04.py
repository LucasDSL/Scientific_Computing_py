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
the_one_with_most_msgs_quantity = None 
the_one_with_most_msgs = ''
for email in emails: 
    if the_one_with_most_msgs_quantity == None: 
        the_one_with_most_msgs_quantity = emails[email]
    elif emails[email] > the_one_with_most_msgs_quantity: 
        the_one_with_most_msgs_quantity = emails[email]
        the_one_with_most_msgs = email
print(f'{the_one_with_most_msgs} {the_one_with_most_msgs_quantity}')