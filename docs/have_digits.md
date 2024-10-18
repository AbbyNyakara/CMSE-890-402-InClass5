# Have Digits

## Tutorials

- Ensure you have a python environment installed
- Define the `have_digits` function in your python file

- Pass a string`s` as the argument.

```python
def have_digits(s):
    out = 0
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
    return out
```

- The function loops through each character in the string, and checks whether its a digit(number).
- If the string `s` contains a digits using python's inbuilt `isdigit() function`, it prints out `1`, else it will print out a `0`.

## How-to Guide

To determine whether the string contains a digit or not:

1. Call the function with the desired string as the argument.
2. The function returns the True(`1`) if the string contains a digit and False(`0`) if the string does not.

```python
result = have_digit("Hel1o")
print(result)  # Output = 1 (The string 'hello' contains a 1)
```

# References

::: functions.have_digits

## Understanding / Explanation

The `have_digits` function uses a secondary pyhton function `isdigits()` to check whether the string that gets passed contains a number/digit.

- The default result is `0`(False)
- The function loops through each digit in the string
- It checks whether each of the characters in the string is a digit.
- If the function is a digit, the fucntion will evaluate to `True` and return `1`.
