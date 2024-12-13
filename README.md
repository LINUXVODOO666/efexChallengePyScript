# Number Validation and Addition

This script validates and adds two floating-point numbers. It ensures that:
- The numbers are greater than 0.1.
- The numbers are less than 10⁶.
- The numbers have no more than 8 decimal places.

## Functions

- **`validate_number(number: float)`**: Validates if the number meets the conditions.
- **`add_numbers(a: float, b: float)`**: Adds two valid numbers.

## Running Tests

To run the tests with `pytest`, use:

```bash
pytest test.py