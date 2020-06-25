import requests
import abc
from bs4 import BeautifulSoup

from errors import Not200RequesCode
from parsers._abcparserfabric import AbstractFactory, AbstractParser


class DwParserTop(AbstractParser):

    def _pagination(self) -> str:
        pass

    def _create_request(self) -> requests.PreparedRequest:
        pass

    def parse_content(self, content: str) -> dict:
        pass


class DwParserSearch(AbstractParser):
    """

    NOTE: Go to AbstractSearchParser to see more code
    """

    url = 'https://www.dw.com/research/?languageCode=en&item={keyword}' \
          '&searchNavigationId=9097-1452-32771-2469-30687-101618-8120&sort=DATE&' \
          'resultsCounter={counter}'

    base_url = 'https://www.dw.com'

    def _pagination(self):
        raise NotImplementedError('This method are not implemet because DW give as'
                                  'so big response as we need')

    def _create_request(self) -> requests.PreparedRequest:
        if self.is_paginate:
            url = self.url.format(keyword=self.keyword, counter=500)
        else:
            url = self.url.format(keyword=self.keyword, counter=100)
        return requests.Request(url=url, method='GET').prepare()

    def parse_content(self, content, depth=0):
        soup = BeautifulSoup(content)
        blocks = soup.find_all('div', {'class': 'searchResult'})

        data = []

        for block in blocks:
            t = {
                'url': self.base_url + block.find('a')['href'],
                'title': block.find('h2').get_text(),
                'text': block.find('p').get_text(),
                'pub_date': block.find('span', {'class': 'date'}).get_text()
            }
            data.append(t)
        return data


class DwParsersFactory(AbstractFactory):

    def create_search_parser(self) -> AbstractParser:
        return DwParserSearch()

    def create_top_parser(self) -> AbstractParser:
        return DwParserTop()


# class BbcParsersFactory(AbstractFactory):
#     pass
