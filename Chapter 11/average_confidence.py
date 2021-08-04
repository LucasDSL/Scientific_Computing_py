import re 
file_handler = open(input('Enter file name: '))
confidence_values = list()
for line in file_handler:
    line = line.rstrip()
    confidence_val_lines = re.findall('X-.*-Confidence:\s([0-9.]*)', line)
    for val in confidence_val_lines:
        if val not in confidence_values: 
            confidence_values.append(val)
total_confidence = number_of_confidences = 0
for val in confidence_values: 
    total_confidence += float(val) 
    number_of_confidences += 1
average_confidence = round(total_confidence/number_of_confidences, 5)
print(average_confidence)