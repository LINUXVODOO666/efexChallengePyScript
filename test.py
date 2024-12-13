import pytest
from main import add_numbers

def test_valid_cases():
    # evaluates cases when numbers are within the valid range
    assert add_numbers(2.3, 1.9) == 4
    assert add_numbers(2.34, 5.7) == 8

def test_numbers_less():
    # evaluates cases when one or both of the numbers are less than 0.1
    with pytest.raises(ValueError, match="Number must be greater than 0.1"):
        add_numbers(0.001, 2.0)
    
    with pytest.raises(ValueError, match="Number must be greater than 0.1"):
        add_numbers(0.001, 0.02)

def test_number_maximum():
    # evaluates cases when one or both of the numbers are greater than 10⁶
    with pytest.raises(ValueError, match="Number must be less than 10⁶"):
        add_numbers(10**7, 5.6)
    
    with pytest.raises(ValueError, match="Number must be less than 10⁶"):
        add_numbers(10**6, 1.4)

def test_number_digit_place():
    # evaluates cases when one or both of the numbers have more than 8 decimal places
    with pytest.raises(ValueError, match="Number must have a maximum of 8 decimal places"):
        add_numbers(10.123456789, 5.6)
    
    with pytest.raises(ValueError, match="Number must have a maximum of 8 decimal places"):
        add_numbers(9.1111111111, 1.4)