def long_substraction(a: int, b: int):
    #Goal: show long addition
    result = []
    borrow = 0
    step = 1

    #Step 1: Create digit array out of each number
    left_number_digit = list(str(a))
    right_number_digit = list(str(b))

    #Step 2: Reverse the lists so we can add from right to left
    left_number_digit.reverse()
    right_number_digit.reverse()

    #Step 3: find the max_length, then question is, do we pad with 0 or do if statements to not borrow 0 values?
    max_length = max(len(left_number_digit), len(right_number_digit))


    #Step 4: Loop through the max_length and substract 1 digit against 1 digit at a time, and adjust value in array if borrowing
    for i in range(max_length):
       print("waiting implementation")

    #Step 5: reverse the result and deliver final result
    result.reverse()
    print("Final Result:\n      "+str(a)+" - "+str(b)+" = "+"".join(result))