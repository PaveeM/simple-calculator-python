# Simple Calculator with Unit Testing & Git Hooks

A robust Python-based calculator demonstrating advanced mathematical operations, comprehensive unit testing, and automated Git lifecycle management.

## 🚀 Features

- **Basic Operations:** Addition, Subtraction, Multiplication, Division.
- **Advanced Math:**
  - **Power:** Calculate base raised to an exponent.
  - **Square Root:** Safe calculation with negative number detection.
  - **Percentage:** Easy percentage calculations.
- **Safety First:** Built-in error handling for division by zero and invalid square roots.

## 🧪 Unit Testing

This project uses Python's built-in `unittest` framework to ensure reliability.

### Running Tests Manually
```bash
python3 test_calculator.py
```

## ⚓ Git Pre-push Hook

One of the key features of this project is the automated quality gate. A **Git Pre-push Hook** is configured to run all unit tests before any code is pushed to a remote repository.

- **How it works:** When you run `git push`, the script in `.git/hooks/pre-push` executes.
- **Enforcement:** If even a single test fails, the push is automatically rejected, preventing broken code from reaching the server.

## 🛠 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PaveeM/simple-calculator-python.git
   cd simple-calculator-python
   ```

2. **Run the calculator:**
   ```bash
   python3 calculator.py
   ```

## 📂 Project Structure

- `calculator.py`: Core logic and mathematical functions.
- `test_calculator.py`: Test suite for all functions.
- `.git/hooks/pre-push`: Automation script for push validation.
