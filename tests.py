import unittest
import parser
import random
from utils import user_agents_list, get_currency_to_ruble_value


user_agent = random.choice(user_agents_list)


class Test(unittest.TestCase):

    def test_response(self):
        response = parser.get_html(parser.URL, user_agent)
        self.assertEqual(response.status_code, 200)

    def test_currency(self):
        dollar = get_currency_to_ruble_value('usd')
        euro = get_currency_to_ruble_value('eur')
        self.assertEqual(type(dollar), float) and self.assertEqual(type(euro), float)
