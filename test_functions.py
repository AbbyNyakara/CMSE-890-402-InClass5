import pytest
from example_functions import my_adder, my_thermo_stat, have_digits


@pytest.mark.parametrize("num1, num2, num3, summation", [(2, 3, 4, 9), (-1, -10, 3, -8), (-2, -7, -4, -13)])
def test_my_adder(num1, num2, num3, summation):
    output = my_adder(num1, num2, num3)
    assert (output == summation)


@pytest.mark.parametrize("temp, desired_temp, status", [(75, 75, "off"), (60, 85, "Heat"), (35, 29, "AC")])
def test_my_thermo_stat(temp, desired_temp, status):
    output = my_thermo_stat(temp, desired_temp)
    assert (output == status)


@pytest.mark.parametrize("test_string, has_digit", [("a5by", True), ("23", True), ("Gigi", False)])
def test_have_digits(test_string, has_digit):
    output = have_digits(test_string)
    assert (output == has_digit)


