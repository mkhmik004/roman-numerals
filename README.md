# Roman Numeral Converter

This Python function converts an integer (up to 4000) into its Roman numeral equivalent. Roman numerals are a combination of the following symbols:

- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

The function ensures proper conversion based on traditional Roman numeral rules, handling subtractive combinations like "IV" (4), "IX" (9), "XL" (40), "XC" (90), "CD" (400), and "CM" (900).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Testing](#testing)
- [License](#license)

## Installation

You don't need any external libraries for this function. Simply copy the function code into your project.

## Usage

This function takes an integer between 1 and 4000 and returns the equivalent Roman numeral as a string.

### Function signature:

```python
def int_to_roman(num: int) -> str:
