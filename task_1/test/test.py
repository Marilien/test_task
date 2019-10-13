import unittest
from task_1.solution.task_1 import is_pld


class MyTestCase(unittest.TestCase):
    def test_registers(self):
        self.assertEqual(is_pld('Maria', 'Arima'), False)
        self.assertEqual(is_pld('Session', 'osseSin'), True)



    def test_sizes(self):
        self.assertEqual(is_pld('maria', 'arimaaaaaa'), False)
        self.assertEqual(is_pld('mariaaaaaaa', 'arimaaaaaaa'), True)


    def test_done(self):
        self.assertEqual(is_pld("Maria", "ariMa"), True)
        self.assertEqual(is_pld("MirrOr", "irOMrr"), True)



if __name__ == '__main__':
    unittest.main()
