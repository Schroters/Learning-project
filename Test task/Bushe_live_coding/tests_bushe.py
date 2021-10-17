import unittest
from live_coding_bushe import bushe


class TestBushe(unittest.TestCase):
    def test_check_bushe_numb(self):
        print('Test check of bushe numbers')
        self.assertEqual(bushe(19), (True, 'Число стало равным одному, это успех'))
        self.assertEqual(bushe(20), (False, 'Невозможно, бесконечность'))
        self.assertEqual((bushe(0)), (False, 'Число не подходит под условия. Число отрицательное или равно нулю'))


if __name__ == '__main__':
    unittest.main()

