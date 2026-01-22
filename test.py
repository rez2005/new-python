import unittest
from test_function import city_country
class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = city_country('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile')
    def test_city_country_population(self):
        result = city_country('Santiago', 'Chile', '5000000')
        self.assertEqual(result, 'Santiago, Chile - population 5000000')

from test_function import employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = employee('John', 'Doe', 60000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 65000)

    def test_give_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.salary, 70000)
if __name__ == '__main__':
    unittest.main()