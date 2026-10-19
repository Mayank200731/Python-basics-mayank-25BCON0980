# Python-basics-mayank-25BCON0980

A small collection of beginner Python examples (and one C example) demonstrating basic programming concepts.

## Contents

- `factorial.py` — currently contains a C program that calculates the factorial of a number (file extension `.py` was used accidentally).
- `fibonacci.py` — Python script that prints the Fibonacci series up to n terms.
- `structure_to_dictionary.py` — Python example that converts a simple class instance to a dictionary.

## Requirements

- Python 3.x — for `fibonacci.py` and `structure_to_dictionary.py`
- GCC (or any C compiler) — to compile and run the program in `factorial.py` as it is written in C

## Usage

1) Factorial (file: `factorial.py`)

The file currently contains C code that computes the factorial of n (n is set to 5 in the source). To compile and run it:

```bash
# Compile (rename when compiling is helpful)
gcc factorial.py -o factorial

# Run
./factorial
# Expected output:
# Factorial of 5 = 120
```

Note: It's recommended to rename `factorial.py` to `factorial.c` so the file extension matches the language. If you prefer a Python implementation, replace the contents with a Python factorial function or ask for help to add one.

2) Fibonacci (file: `fibonacci.py`)

This is a simple Python program that asks for the number of terms and prints the Fibonacci series on a single line.

Run:

```bash
python3 fibonacci.py
# Enter the number of terms, e.g. 5
# Output example:
# 0 1 1 2 3
```

3) Convert structure to dictionary (file: `structure_to_dictionary.py`)

A small demonstration of turning a class instance into a dictionary using `vars()` (or `.__dict__`). The script prints the resulting dictionary.

Run:

```bash
python3 structure_to_dictionary.py
# Expected output:
# {'name': 'Mayank', 'age': 20, 'branch': 'CSE'}
```

## Notes

- If you'd like, I can:
  - Convert the `factorial.py` C code into a proper `factorial.c` file and update the repository accordingly, or
  - Replace it with a Python implementation and keep the `.py` extension.

- Feel free to tell me which option you prefer and I will update the repository.
