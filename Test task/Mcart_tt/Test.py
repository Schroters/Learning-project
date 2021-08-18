import unittest
import currency_exchange_rate


class Test_exchange_rate(unittest.TestCase):
    def test_date_conversion(self):
        self.assertEqual(currency_exchange_rate.date_conversion('2020-12-14'), '14/12/2020')
        self.assertEqual(currency_exchange_rate.date_conversion('2020-01-09'), '09/01/2020')

    def test_date_check(self):
        self.assertTrue(currency_exchange_rate.date_check('2020-12-14'))
        self.assertFalse(currency_exchange_rate.date_check('2020-13-02'))
        self.assertFalse(currency_exchange_rate.date_check('2020-12-32'))
        self.assertFalse(currency_exchange_rate.date_check('s'))

    def test_currency_difference(self):
        self.assertEqual(currency_exchange_rate.currency_difference('2020-08-20', '2020-08-21', 'HKD'),
                         'Нет значений за выбранный период')
        self.assertEqual(currency_exchange_rate.currency_difference('2020-08-20', '2021-08-20', 'USD'),
                         'Курс за 2020-08-20 составляет: 73,2392 за 1 USD\n'
                         'Курс за 2021-08-20 составляет: 73,4633 за 1 USD\n'
                         'Разница состовляет: -0.22410000000000707 ₽')

