from function_motorcycle import calculate_monthly_payment , validate_price
import pytest

def test_calculate_monthly_payment1():
    assert round(calculate_monthly_payment(100000, 20000), 2) == 6848.6

def test_price_int_input_0_input():
    assert validate_price(0) == "Invalid input. Please enter a positive number."

def test_price_negative_input():
    assert validate_price(-100000) == "Invalid input. Please enter a positive number."

def test_price_negative_float():
    assert validate_price(-1000.00) == "Invalid input. Please enter a positive number."

def test_price_str_input1():
    assert validate_price("abc") == "Invalid input. Please enter a positive number."

def test_price_str_input2():
    assert validate_price("กขค") == "Invalid input. Please enter a positive number."

def test_price_str_input3():
    assert validate_price("@#!%&") == "Invalid input. Please enter a positive number."