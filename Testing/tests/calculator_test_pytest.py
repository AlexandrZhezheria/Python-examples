import pytest

from Testing.Lessons.Unittest_Lesson import calculator


def test_plus():
    assert calculator("2 + 2") == 4


def test_minus():
    assert calculator("3 - 2") == 1


def test_multi():
    assert calculator("4 * 2") == 8


def test_divide():
    assert calculator("8 / 4") == 2


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator("asdqwezxc")
    assert "Выражение должно содержать хотя бы один знак (+-/*)" == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator("2 + 2 + 2")
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


def test_many_signs():
    with pytest.raises(ValueError) as error:
        calculator("3 + 2 * 10")
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
