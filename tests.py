import unittest
import parser
from bs4 import BeautifulSoup


class Test(unittest.TestCase):

    def test_response(self):
        response = parser.get_html(parser.URL)
        self.assertEqual(response.status_code, 200)


    def test_vacancy_count(self):
        html = parser.get_html(parser.URL).text
        soup = BeautifulSoup(html, "lxml")
        vac_count = soup.find("h1", {"class": "header"}).text
        vac_count = int(vac_count.split()[0])
        self.assertEqual(len(parser.parse_data()), vac_count)