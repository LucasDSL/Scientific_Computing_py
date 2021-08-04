import re 
file_name = input('Enter file: ')
try: 
    file_handler = open(file_name)
except: 
    print(f'File not found: {file_name}')
    quit()
quantity_revisions = 0
total_revision = 0
for line in file_handler: 
    line = line.rstrip()
    number_line = re.findall('New Revision: ([0-9]*)', line)
    if len(number_line) == 0: continue 
    quantity_revisions += 1
    total_revision += float(number_line[0])
average_revision = round(total_revision/quantity_revisions, 7)
print(average_revision)
