import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "p", "Skyro"),
    ("Skypro", "o", "Skypr")])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) ==expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "p", ""),
    ("Skypro", "t", "Skypro")])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) ==expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, bool", [
    ("Skypro", "p", True),
    ("Skypro", "u", False)])
def test_contains_symbol(string, symbol, bool):
    assert string_utils.contains(string, symbol) ==bool


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, bool", [
    ("Skypro", "--", False),
    ("1234", "  ", False)])
def test_contains_symbol_negative(string, symbol, bool):
    assert string_utils.contains(string, symbol) ==bool


@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ("   Skypro", "Skypro"),
    ("         Skypro", "Skypro")])
def test_trim(string, expected):
    assert string_utils.trim(string) ==expected


@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("Skypro", "Skypro"),
    ("Skypro   ", "Skypro   ")])
def test_trim_negative(string, expected):
    assert string_utils.trim(string) ==expected