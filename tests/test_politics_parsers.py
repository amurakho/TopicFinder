import unittest
import requests

from parsers import dwparser
from parsers._abcparserfabric import AbstractSearchParser
from parameterized import parameterized_class

search_parsers = (
    {
        'parser': dwparser.DwParserSearch,
        'url': 'https://www.dw.com/search/en?searchNavigationId=9097&languageCode=en&origin=gN&item=test'
    },
)


@parameterized_class(search_parsers)
class SearchParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.parser = cls.parser()
        cls.parser.keyword = 'test'

    def test_parse_content(self):

        content = requests.get(self.url).content
        res = self.parser.parse_content(content)
        self.assertNotEqual(res, [])
        self.assertNotEqual(res[0], {})
        self.assertTrue(res[0].get('url'))
        self.assertTrue(res[0].get('title'))
        self.assertTrue(res[0].get('text'))
        self.assertTrue(res[0].get('pub_date'))


class TopParserTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
