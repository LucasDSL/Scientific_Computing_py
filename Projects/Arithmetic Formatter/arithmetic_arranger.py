def arithmetic_arranger(list_sums, option_argument=True):
    # Transforming all string on list of strings: 
    for i in range(0, len(list_sums)):
        list_sums[i] = list_sums[i].split(" ")    
    
    # Looking for errors:
    if len(list_sums) > 5: 
        return "Error: Too many problems." 
    for sum in list_sums: 
        if sum[1] != "+" and sum[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if len(sum[0]) > 4 or len(sum[2]) > 4: 
            return "Error: Numbers cannot be more than four digits."
        try: 
            int(sum[0])
            int(sum[2])
        except: 
            return "Error: Numbers must only contain digits."

    if not option_argument:
        return ""
    string_return = ""
    # Formating the first line of the result. 
    for sum in list_sums:
        # Getting the size of the bigger number: 
        sz_n1 = len(sum[0]) # Size in digits of the first number.
        sz_n2 = len(sum[2]) # Size in digits of the second number.
        size_bigger_num = sz_n1 if sz_n1 > sz_n2 else sz_n2
        sum.append(size_bigger_num)
        string_return += f"{sum[0]:>{size_bigger_num + 2}}" # Plus two spaces (1 for the
        # operation sign below and one for the blank space after it )
        if list_sums[-1] == sum:
            string_return += "\n"
        else:
            string_return += "    "

    # Formating the second line of the result
    for sum in list_sums:
        string_return += f"{sum[1]} {sum[2]:>{sum[3]}}" # Sum[3] is the 
        # equivalent of the size_bigger_num of the current two operands
        if list_sums[-1] == sum:
            string_return += "\n"
        else:
            string_return += "    "

    # Formating the line below the operation: 
    for sum in list_sums:
        string_return += "-" * (sum[3] + 2) # Plus two again (1 sign + 1 blank space)
        if list_sums[-1] == sum:
            string_return += "\n"
        else:
            string_return += "    "

    # Getting the result from the sum of the two operands: 
    for sum in list_sums:
        current_sum = 0
        if sum[1] == "+":
            current_sum += int(sum[0]) + int(sum[2])
        else: 
            current_sum += int(sum[0]) - int(sum[2])
        current_sum = str(current_sum)
        size_current_sum = len(current_sum)
        string_return += f"{current_sum:>{sum[3] + 2}}"
        if list_sums[-1] == sum:
            string_return += "\n"
        else:
            string_return += "    "

    return string_return

