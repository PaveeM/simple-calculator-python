# Bug Report - Simple Calculator

## 1. Inconsistent Exception Types
- **Issue:** The `power` function raised `ZeroDivisionError` when the base was zero and the exponent was negative. This was inconsistent with the `divide` function, which raises `ValueError` for division by zero.
- **Fix:** Added a check in `power` to raise `ValueError` for zero base with negative exponents.

## 2. Unexpected Complex Number Results
- **Issue:** The `power` function returned complex numbers when given a negative base and a fractional exponent (e.g., `power(-2, 0.5)`). In a "Simple Calculator" context where `square_root` of a negative number raises `ValueError`, this behavior was inconsistent and potentially confusing.
- **Fix:** Added a check in `power` to raise `ValueError` when a negative base is raised to a fractional exponent, ensuring only real numbers are returned or an error is raised.

## 3. Missing Test Coverage
- **Issue:** Several edge cases for the `power` function were not covered in `test_calculator.py`, allowing the inconsistencies mentioned above to go unnoticed.
- **Fix:** Expanded `test_power` in `test_calculator.py` to include tests for these edge cases and verify they raise the expected `ValueError`.
