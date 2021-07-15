def counting(string, letter):
    times_letter = 0
    for let in string:
        if let == letter: 
            times_letter += 1
    print(times_letter)

counting('banana', 'a')