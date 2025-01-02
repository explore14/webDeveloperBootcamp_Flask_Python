def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    else:
        return dividend/divisor
    
def calculate(*values,operator):
    return operator(*values)


x= calculate(14,2,operator= divide)
print(x)

##########################################

