string = 'X-DSPAM-Confidence:0.8475'
num_beginning = string.find(':') + 1
num_end = len(string)
num = float(string[num_beginning: num_end])
print(num)
print(type(num))

