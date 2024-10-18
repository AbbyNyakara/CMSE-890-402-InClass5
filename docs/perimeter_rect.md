# Perimeter of a rectangle

## Tutorial

- Ensure you have a python environment installed. run `python --version` to check
- Define the `perimeter_of_rect` function in your python file
- Pass the width and height of the rectangle as arguments.

```python
def perimeter_of_rectangle(width:float, height:float) -> float:
    perimeter = (2 * width) + (2 * height)
    return perimeter
```

- With the fucntion Created, you can now use it as in the example shown below:

```python
# Example 1
given_width = 12
given_height = 3
area = perimeter_of_rect(given_width, given_height)
print(area) #EXPECTED OUTPUT = 30

# Example 2
given_width = 10.2
given_height = 2.1
area = perimeter_of_rect(given_width, given_height)
print(area) #Expected output = 24.6
```

## How-to-Guides

To calculate the perimeter of a rectangle using the `perimeter_of_rect` function:

1. Call the function with width and height of the rectangle as arguments.
2. The function returns the perimeter.

```python
perimeter = perimeter_of_rect(2, 5)
print(perimeter)  # Output = 14
```

## Reference:

::: functions.perimeter_of_rect

## Understanding / Explanation

The perimeter of a rectangle is the distance around a rectangle. And since the rectangle has 2 sides each of equal lengths, we use the formula `perimeter = 2xlength + 2xwidth` This function is a python implementation of this basic mathematical function.
