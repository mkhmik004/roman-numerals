# Roman Numeral Converter

## Overview

This project contains a Python function that converts an integer to its corresponding Roman numeral. Roman numerals use a combination of specific symbols (I, V, X, L, C, D, M) to represent numbers. The function follows both the additive and subtractive rules of Roman numeral formation.

## Features

Converts integers to Roman numerals.
Handles both small and large numbers (up to 3999, which is the limit for standard Roman numerals).
Handles subtractive combinations like IV (4), IX (9), and others.
Simple and easy-to-understand implementation using Python.

## Roman Numeral Rules

### Subtractive Rule:
If a smaller numeral comes before a larger one, subtract the smaller numeral from the larger.
Example: IV = 4 (5 - 1) and IX = 9 (10 - 1).

### Additive Rule:
If a smaller numeral comes after a larger numeral, add them together.
Example: VI = 6 (5 + 1) and XI = 11 (10 + 1).

## Functionality 

The program defines a function called to_roman_numeral in the number_representations.py file that:

Takes an integer as input.
Returns the Roman numeral representation as a string.

## Technology

Python

Unit testing with unittest

## Installation

You don't need any external libraries for this function. Simply copy the function code into your project.

## Usage

This function takes an integer between 1 and 4000 and returns the equivalent Roman numeral as a string.

### Function signature:
def to_roman_numeral(num: int) -> str:

## Acknowledgement 

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed.
