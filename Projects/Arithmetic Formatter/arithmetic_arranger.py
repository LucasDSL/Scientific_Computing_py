def arithmetic_arranger(list_sums):
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
            sum[0] = int(sum[0])
            sum[2] = int(sum[2])
        except: 
            return "Error: Numbers must only contain digits."

    def return_string_formatted_to_size(list_str, line=1):
        bigger_str = len(list_str[0]) if list_str[0] >= list_str[2]else len(list_str[2])

        ''' Return the string formated to the size of the number + 2 spaces (1 for the operand sign
         and 1 for the space between the sign and the number on the second line ) '''
        if line == 1:
            if bigger_str == 1: 
                return "{first_line_element:>3}".format(first_line_element = list_str[0]) 
            elif bigger_str == 2: 
                return "{first_line_element:>4}".format(first_line_element = list_str[0])   
            elif bigger_str == 3: 
                return "{first_line_element:>5}".format(first_line_element = list_str[0])   
            elif bigger_str == 4: 
                return "{first_line_element:>6}".format(first_line_element = list_str[0]) 

    string_return = ""
    # Formating the first line of the result. 
    for sum in list_sums:
        string_return += "{first_line_element:>6}".format(first_line_element = sum[0]) 
        string_return += "    "
    string_return += "\n"
    # Formating the second line of the result
    for sum in list_sums:
        string_return += "{operation_sign} {operand:>4}".format(operation_sign = sum[1],
        operand = sum[2])
        string_return += "    "
    string_return += "\n"
    # Formating the line below the operation: 
    for sum in list_sums:
        pass
    print(string_return)

