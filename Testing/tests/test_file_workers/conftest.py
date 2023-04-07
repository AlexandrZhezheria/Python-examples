import pytest


@pytest.fixture(autouse=True)
def clean_test_file():
    with open("tests/testfile.txt", "w"):
        pass
