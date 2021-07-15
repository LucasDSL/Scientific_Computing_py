type_of_line = 'X-DSPAM-Confidence: 0.8475'
file_name = input('Enter file name: ')
try: 
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()
sum_spam = total_spam = 0
for line in file_handler: 
    line = line.rstrip()
    if line.startswith(type_of_line[0:19]): # See if the line starts accordingly to the type_of_line
        sum_spam += float(line[20:]) # Get the number o spam trust and sum it to the total
        total_spam += 1

print(f'Average spam trust: {sum_spam/total_spam}')