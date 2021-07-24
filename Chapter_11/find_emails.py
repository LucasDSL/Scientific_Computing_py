# using regex to find emails in a file 
import re 
file_handler = open(input('enter file: '))
emails = list()
for line in file_handler:
    line = line.rstrip()
    emails_line = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    for e in emails_line:
        if e not in emails: 
            emails.append(e)
print(emails)