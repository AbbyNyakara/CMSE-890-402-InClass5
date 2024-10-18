# My Adder

# Tutorials

- Ensure you have a python environment installed
- Define the `my_adder` function in your python file

- Pass the 3 numbers `a, b, c` as argumnets/inputs

```python
def my_adder(a: float, b: int, c: float) -> float:
    sum_nums = a + b + c
    return sum_nums
```

- With the function defined, you can now use it as in the example shown below:

```python
# Example 1
a = 1
b = 5
c = 7
sum_nums = my_adder(1, 5, 7)
print(sum_nums) #EXPECTED OUTPUT = 13
```

## How-to-Guide:

The `my_adder` function is used to calculate the sum of 3 numbers.

1. Call the function passing in the 3 numbers being added as inputs to the functions `a, b, c`
2. The function returns the sum of the 3 numbers.

```python
print(my_adder(2, 3, 4))
# The expected output is - 9
```

# References

::: functions.my_adder

## Understanding / Explanation

The sum of 3 numbers is calculated by adding them up. This function is a python implementation of this basic mathematical function.

The formula is: `sum = first_number + second_number + third_number`
