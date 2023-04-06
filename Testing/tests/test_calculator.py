from unittest import TestCase, main
from Testing.Lessons.Unittest_Lesson import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("2 + 2"), 4)

    def test_minus(self):
        self.assertEqual(calculator("3 - 2"), 1)

    def test_multi(self):
        self.assertEqual(calculator("4 * 2"), 8)

    def test_divide(self):
        self.assertEqual(calculator("8 / 4"), 2)


if __name__ == '__main__':
    main()
