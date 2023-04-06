from unittest import TestCase, main
from Testing.Lessons.Unittest_Lesson import calculator

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("2 + 2"), 4)


if __name__ == '__main__':
    main()
