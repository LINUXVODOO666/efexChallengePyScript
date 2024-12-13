

def validate_number(number:float):
    if not number > 0.1:
        raise ValueError("Number must be greater than 0.1")
    if not number < 10**6:
        raise ValueError("Number must be less than 10⁶")
    
    decimal_length = len(str(number).split('.')[1]) 
    if decimal_length > 8:
        raise ValueError("Number must have a maximum of 8 decimal places")



def add_numbers(a:float,b:float):
    validate_number(a)
    validate_number(b)
    return int((float(a)+float(b)))