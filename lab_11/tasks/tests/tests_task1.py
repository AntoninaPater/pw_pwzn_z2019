import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

test_run_good_data = [("+", 2, 3, 5),
                      ("-", 2, 3, -1),
                      ("*", -2, 3, -6),
                      ("/", -2, 4, -0.5)]

test_run_bad_data = [("+", 2, "a", NotNumberArgument),
                     ("-", "b", 3, NotNumberArgument),
                     ("*", -2, None, EmptyMemory),
                     ("/", -2, 0, CalculatorError),
                     ("/", -2, 0.0, CalculatorError),
                     ("^", -2, 4, WrongOperation),
                     (2, "*", 4, WrongOperation),
                     (2, -2, 4, WrongOperation)]


@pytest.fixture()
def calculator():
    return Calculator()


@pytest.mark.parametrize("operator, arg1, arg2, expected", test_run_good_data)
def test_run_good_input(operator, arg1, arg2, expected, calculator):
    result = calculator.run(operator, arg1, arg2)
    assert result == expected


@pytest.mark.parametrize("operator, arg1, arg2, expected", test_run_bad_data)
def test_run_bad_input(operator, arg1, arg2, expected, calculator):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)


def test_memory(calculator: "Calculator"):
    calculator.run("+", 2, 3)
    assert calculator._short_memory == 5
    calculator.memorize()
    assert calculator.memory == 5
    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory
