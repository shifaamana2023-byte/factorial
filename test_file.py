import unittest

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


class TestProgram(unittest.TestCase):

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_2(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_3(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_4(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_prime_2(self):
        self.assertTrue(is_prime(2))

    def test_prime_5(self):
        self.assertTrue(is_prime(5))

    def test_not_prime_4(self):
        self.assertFalse(is_prime(4))

    def test_not_prime_1(self):
        self.assertFalse(is_prime(1))

    def test_not_prime_0(self):
        self.assertFalse(is_prime(0))


if __name__ == '__main__':
    unittest.main()