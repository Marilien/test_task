import unittest
from task_1.solution.task_1 import is_pld


class MyTestCase(unittest.TestCase):
    def test_registers(self):
        self.assertEqual(is_pld('Maria', 'Arima'), False)

    def test_sizes(self):
        self.assertEqual(is_pld('Maria', 'Arimaaaaaa'), False)


if __name__ == '__main__':
    unittest.main()
