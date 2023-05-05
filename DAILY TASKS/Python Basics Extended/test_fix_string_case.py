import pytest

from fix_string_case import fix_string_case


def test_should_return_type_str():
    assert (
        isinstance(fix_string_case("aaIo"), str) is True
    ), "Function `fix_string_case` should return string"


@pytest.mark.parametrize(
    "word, modified_word",
    [
        ("", ""),
        ("a", "a"),
        ("OG", "OG"),
        ("maTE", "mate"),
        ("OuaeI", "ouaei"),
        ("oUAEi", "OUAEI"),
        ("aei ou", "aei ou"),
        ("208903", "208903"),
        ("ACADemy", "ACADEMY"),
        ("aabbbcccE", "aabbbccce"),
        ("QWERTYUIOP", "QWERTYUIOP"),
        ("f  jj  MM A", "f  jj  mm a"),
        ("MATE academy 2022 @)@@", "mate academy 2022 @)@@"),
        ("THAT"S fine, I STUDY here!", "THAT"S FINE, I STUDY HERE!"),
    ],
)
def test_fix_string_case(word, modified_word):
    assert fix_string_case(word) == modified_word, (
        f"Function "fix_string_case" should return {modified_word} "
        f"when sentence is {word}"
    )
