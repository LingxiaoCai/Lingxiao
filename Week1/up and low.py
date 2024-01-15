"""
Write a Python function named case_counter that counts the number of uppercase and lowercase letters in a given string.

The function should calculate and return two numbers: the count of uppercase letters and the count of lowercase letters in the string.
If there are no letters of a particular case (uppercase or lowercase) in the string, the function should return 0 for that case.
Non-alphabetic characters in the string should be ignored and not counted.
"""


def case_counter(text):
    upper = 0
    lower = 0
    for l in text:
        if l.islower() == True:
            lower += 1
        elif l.isupper() == True:
            upper += 1
    print(f'Uppercase letters: {upper}, Lowercase letters: {lower}')
    # Your code goes here
    pass


# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON") # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python") # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0