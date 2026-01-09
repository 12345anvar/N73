# 1
def greet(name: str, age: int) -> str:
    """
    Return welcoming text based on given name and age
    :param name: any string
    :param age: any integer
    :return: text
    """
    return f"Hello {name}, you are {age} years old"


# 2
def add_numbers(a: int | float, b: int | float) -> int | float:
    """
    Sum of two numbers
    :param a: any integer or float number
    :param b: any integer or float number
    :return: result
    """
    return a + b


# 3
def get_user_info() -> dict[str, str | int]:
    """
    Get user info as a dict format
    :return: dict data
    """
    return {"name": "Alice", "age": 25}


# 4
def sum_list(numbers: list[int | float]) -> int | float:
    """
    Sum of number in the list given
    :param numbers: list of any integer or float numbers
    :return: result
    """
    total: int = 0
    for n in numbers:
        total += n
    return total


# 5
def find_max(numbers: list[int | float]) -> int | float | None:
    """
    Finding the maximum number in the given list or None if list is empty
    :param numbers: list of any integer or float numbers
    :return: maximum number
    """
    if not numbers:
        return None
    return max(numbers)


# 6
def is_even(n: int) -> bool:
    """
    True if the number is even else False
    :param n: any integer number
    :return: True or False
    """
    return n % 2 == 0


# 7
from typing import Any


def merge_dicts(d1: dict[Any, Any], d2: dict[Any, Any]) -> dict[Any, Any]:
    """
    Updating given second dictionary with given first dictionary
    :param d1: any dict,
    :param d2: any dict
    :return: updated second dict
    """
    result = d1.copy()
    result.update(d2)
    return result


# 8
def filter_positive(numbers: list[int | float]) -> list[int | float]:
    """
    Return filtered by positivity of number as a list
    :param numbers: the list of any float or int number
    :return: result
    """
    return [n for n in numbers if n > 0]


# 9
def get_full_name(first_name: str, last_name: str) -> str:
    """
    Return full name
    :param first_name: any string,
    :param last_name: any string
    :return: full name
    """
    return f"{first_name} {last_name}"


# 10
def average(numbers: list[int | float]) -> float:
    """
    Average value of numbers
    :param numbers: list of any integer or float number,
    :return: float number
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Uyga vazifa

# 1
def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiply two numbers
    :param a:any number,
    :param b:any number,
    :return:result number
    """
    return a * b


# 2
def repeat_string(s: str, times: int) -> str:
    """
    Repeat a string a given number of times.
    :param s: The string to repeat.
    :param times: How many times to repeat.
    :return: The concatenated result.
    """
    return s * times


# 3
def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filter a list and return only the even numbers.
    :param numbers: A list of integers.
    :return: A new list containing only even integers.
    """
    return [n for n in numbers if n % 2 == 0]


# 4
def find_min_max(numbers: list[int | float]) -> tuple[int | float, int | float] | tuple[None, None]:
    """
    Find the minimum and maximum values in a list.
    :param numbers: A list of numbers (integers or floats).
    :return: A tuple containing (min, max), or (None, None) if the list is empty.
    """
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


# 5
def concatenate_strings(strings: list[str]) -> str:
    """
    Join a list of strings into a single string separated by spaces.
    :param strings: A list of string elements.
    :return: A single concatenated string.
    """
    return " ".join(strings)


# 6
def square_dict(numbers: dict[str | int, int | float]) -> dict[str | int, int | float]:
    """
    Create a new dictionary with the squares of the original values.
    :param numbers: A dictionary where values are numbers.
    :return: A dictionary with the same keys but squared values.
    """
    return {k: v ** 2 for k, v in numbers.items()}


# 7
def reverse_list(items: list) -> list:
    """
    Return a new list with the elements in reverse order.
    :param items: The original list of elements.
    :return: A list containing the same elements in reverse.
    """
    return items[::-1]


# 8
def count_occurrences(items: list, value: any) -> int:
    """
    Count how many times a specific value appears in a list.
    :param items: The list to search through.
    :param value: The value to look for.
    :return: The total count of occurrences.
    """
    return items.count(value)


# 9
def flatten_list_of_lists(lists: list[list]) -> list:
    """
    Convert a nested list (list of lists) into a single flat list.
    :param lists: A list containing other lists as elements.
    :return: A 1D list containing all individual items.
    """
    return [item for sublist in lists for item in sublist]


# 10
def divide(a: int | float, b: int | float) -> float | None:
    """
    Divide two numbers and handle division by zero.
    :param a: The dividend (number to be divided).
    :param b: The divisor (number to divide by).
    :return: The quotient as a float, or None if the divisor is zero.
    """
    if b == 0:
        return None
    return a / b
