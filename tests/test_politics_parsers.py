import unittest
import requests

from parsers import dwParser, cnnParser
from parsers._abcparserfabric import AbstractSearchParser
from parameterized import parameterized_class

search_parsers = (
    {
        'parser': dwParser.DwParserSearch,
        'url': 'https://www.dw.com/search/en?searchNavigationId=9097&languageCode=en&origin=gN&item=test'
    },
    # {
    #     'parser': cnnparser.CnnParserSearch,
    #     'url': 'https://edition.cnn.com/search?q=test'
    # },

)

top_parsers = (
    {
        'parser': dwParser.DwParserTop,
    },
    # {
    #     'parser': cnnparser.CnnParserTop,
    # }
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


@parameterized_class(top_parsers)
class TopParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.parser = cls.parser()

    def test_all(self):
        """
        I launch all because the code is simple. and main part is parse_content
        """
        res = self.parser.start_parse()
        self.assertNotEqual(res, [])
        self.assertNotEqual(res[0], {})
        self.assertTrue(res[0].get('url'))
        self.assertTrue(res[0].get('title'))


if __name__ == '__main__':
    unittest.main()
