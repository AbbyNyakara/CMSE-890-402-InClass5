# My thermostat

## Tutorials

- Ensure you have a python environment installed
- Define the `my_thermo_stat` function in your python file

- Pass the width and height of the rectangle as arguments.

```python
def my_thermo_stat(temp: float, desired_temp: float) -> float:
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
```

- With the fucntion Created, you can now use it as in the example shown below:

```python
# Example 1
temp = 65
desired_temp =75
output = my_thermo_stat(65, 75)
print(output) #EXPECTED OUTPUT = 'Heat'

#Example 2
temp = 72
desired_temp =75
output = my_thermo_stat(72, 75)
print(output) #EXPECTED OUTPUT = 'off'

#Example 3
temp = 72
desired_temp =60
output = my_thermo_stat(72, 60)
print(output) #EXPECTED OUTPUT = 'AC'
```

## How-to-Guide:

The `my_thermo_stat` function is used to determine whether a thermostat should be `off`,
whether the `AC` should be on to cool the room or whether there should be `Heat` when the
room is too cold.

1. Call the function passing in the actual temperature `temp` and the desired temperature `desired_temp` as inputs
2. The function returns the status of the thermostat.

```python
print(my_thermo_stat(72, 60))
# The expected output is - AC
```

## References

::: functions.my_thermo_stat

## Understanding / Explanation

`my_thermo_stat` returns the status of the thermostat whether it should be `off, AC or Heat` depending on the `temp` and the `desired_temp`.

If the temp is + or - 5 units within the desired_temp, the thermostat will be `off`
If the temp is more than 5 units reading below the desired_temp, the thermostat will be on `Heat`
If the temp is more than 5 units reading above the desired_temp, the thermostat will be on `AC`
