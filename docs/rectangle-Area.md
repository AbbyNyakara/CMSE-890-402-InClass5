# Area of a rectangle

## Tutorials

- Ensure you have a python environment installed
- Define the `area_of_rectangle` function in your python file

- Pass the width and height of the rectangle as arguments.

```python
def area_of_rectangle(width: float | int, height:float | int) -> float | int:
    return width * height
```

- With the fucntion Created, you can now use it as in the example shown below: 
```python
# Example 1
given_width = 12
given_height = 3
area = area_of_rectangle(given_width, given_height)
print(area) #EXPECTED OUTPUT = 36

#eXAMPLE 2
given_width = 10.2
given_height = 2.1
area = area_of_rectangle(given_width, given_height)
print(area) #Expected output = 21.42
```

## How-to-Guides

To calculate the area of a rectangle using the `area_of_rectangle` function:
1. Call the function with width and height of the rectangle as arguments.
2. The function returns the area.

```python
area = area_of_rectangle(2, 5)
print(area)  # Output = 10
```
## Reference: 
::: functions.area_of_rectangle

## Understanding / Explanation

The area of a rectangle is calculated by multipying the rectangle's width by the height. This function is a python implementation of this basic mathematical function. 

The formula is: `Area = width x Height`



