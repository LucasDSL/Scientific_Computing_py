fhand = open('file_to_read.txt')
for line in fhand:
    line = line.rstrip()
    print(line)