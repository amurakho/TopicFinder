import requests
from bs4 import BeautifulSoup

from const import POLITICS_SITES
from errors import Not200RequesCode
from parsers._abcparserfabric import AbstractFactory, AbstractSearchParser, AbstractTopParser

DW_BASE_URL = POLITICS_SITES.get('dw')


class DwParserTop(AbstractTopParser):

    url = 'https://www.dw.com/en/top-stories/s-9097'

    def parse_blocks(self, blocks, data):
        for block in blocks:
            text_block = block.find('p')
            t = {
                'url': DW_BASE_URL + block.find('a')['href'],
                'title': block.find('h2').get_text(),
                'pub_date': None,
                'text': text_block.get_text() if text_block else None
            }
            data.append(t)

    def parse_content(self, content: bytes):
        soup = BeautifulSoup(content, 'lxml')
        data = []

        # parse main part
        blocks = soup.find_all('div', {'class': 'basicTeaser'})
        self.parse_blocks(blocks, data)

        # parse most read
        blocks = soup.find_all('div', {'class': 'linkList'})
        self.parse_blocks(blocks, data)

        # parse by country
        blocks = soup.find_all('div', {'class': 'searchres'})
        self.parse_blocks(blocks, data)

        return data


class DwParserSearch(AbstractSearchParser):
    """

    NOTE: Go to AbstractSearchParser to see more code
    """

    url = 'https://www.dw.com/research/?languageCode=en&item={keyword}' \
          '&searchNavigationId=9097-1452-32771-2469-30687-101618-8120&sort=DATE&' \
          'resultsCounter={counter}'

    base_url = 'https://www.dw.com'

    def _pagination(self):
        raise NotImplementedError('This method are not implemet because DW give as'
                                  'so big response as we need(counter variable in _create_request'
                                  'for count results)')

    def _create_request(self) -> requests.PreparedRequest:
        if not self.keyword:
            raise NotImplementedError('Need keyword')

        if self.is_paginate:
            url = self.url.format(keyword=self.keyword, counter=500)
        else:
            url = self.url.format(keyword=self.keyword, counter=100)
        return requests.Request(url=url, method='GET').prepare()

    def parse_content(self, content, depth=0):
        soup = BeautifulSoup(content, 'lxml')
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


class ParsersFactory(AbstractFactory):

    def create_search_parser(self) -> AbstractSearchParser:
        return DwParserSearch()

    def create_top_parser(self) -> AbstractTopParser:
        return DwParserTop()
