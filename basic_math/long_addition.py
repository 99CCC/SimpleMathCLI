def long_addition(a: int, b: int):
    #Goal: show long addition
    result = []
    carry = 0
    step = 1

    #Step 1: Create digit array out of each number
    left_number_digit = list(str(a))
    right_number_digit = list(str(b))

    #Step 2: Reverse the lists so we can add from right to left
    left_number_digit.reverse()
    right_number_digit.reverse()

    #Step 3: find the max_length, and then pad shorter list if needed (so we dont get error trying to add NaN)
    max_length = max(len(left_number_digit), len(right_number_digit))
    while len(left_number_digit) < max_length:
        left_number_digit.append('0')
    while len(right_number_digit) < max_length:
        right_number_digit.append('0')

    #Step 4: Loop through the max_length and add 1 and 1 digit, and check for carry overs
    for i in range(max_length):
        digit_l = int(left_number_digit[i])
        digit_r = int(right_number_digit[i])
        part_sum_calc = digit_l+digit_r+carry
        print("Step "+str(step)+"\n     "+str(digit_l)+" + "+str(digit_r)+" + Carry = "+str(part_sum_calc)+" # Carry = "+str(carry))
        step += 1
        if(part_sum_calc >= 10):
            part_sum = str(part_sum_calc%10)
            carry = part_sum_calc // 10
            result.append(part_sum)
            print("     Carry found, adding "+part_sum+" as part of result, and carrying over "+str(carry))
        else:
            result.append(str(part_sum_calc))
            carry = 0
            print("     No carry found, adding "+str(part_sum_calc)+" as part of result")
    
    if(carry != 0):
        result.append(str(carry))

    result.reverse()
    print("Final Result:\n      "+str(a)+" + "+str(b)+" = "+"".join(result))