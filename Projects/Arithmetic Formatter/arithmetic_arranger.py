def arithmetic_arranger(list_sums):
    if len(list_sums) > 5: 
        return "Error: Too many problems."
    # Looking for other errors: 
    for sum in list_sums: 
        sum = sum.split(" ")
        if sum[1] != "+" and sum[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if len(sum[0]) > 4 or len(sum[2]) > 4: 
            return "Error: Numbers cannot be more than four digits."
        try: 
            sum[0] = int(sum[0])
            sum[2] = int(sum[2])
        except: 
            return "Error: Numbers must only contain digits."
        
        

