def replace_last(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        for x in numbers:
            a = numbers[0]
            numbers[0] = numbers[-1]
            numbers.insert(1, a)

            return numbers[0:-1]

        
    
    
