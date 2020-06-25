import requests
import abc
from bs4 import BeautifulSoup

from errors import Not200RequesCode
from parsers._abcparser import Parser


class DwParserTop(Parser):

    def _create_request(self, keyword: str) -> requests.PreparedRequest:
        pass

    def parse_content(self, content: str) -> dict:
        pass

    def start_parse(self) -> dict:
        pass


class AbstractSearchParser(abc.ABC):
    """
    Interface for "search" parsers.

    """
    keyword = ''

    def __init__(self, is_paginate=True, max_depth=10):
        self.is_paginate = is_paginate
        self.max_depth = max_depth


    @abc.abstractmethod
    def _create_request(self):
        """
        Accepts keyword and create request and prepare it for session

        :param keyword:
        :return: prepared request
        """
        pass

    @abc.abstractmethod
    def parse_content(self, content, depth=0):
        """
        Parse content

        :param content:
        :return:
        """
        pass

    @abc.abstractmethod
    def _pagination(self):
        """
        Pagination

        :return:
        """
        pass

    def pass_request(self, request: requests.PreparedRequest) -> bytes:
        """
        Pass reqeust
        (if need - pagination)

        :param request: Prepared request
        :return:
        """
        session = requests.Session()
        response = session.send(request)
        if response.status_code != 200:
            raise Not200RequesCode('Error with search request.'
                                   'Current code is: ', response.status_code)
        return response.content

    def start_parse(self, keyword: str):
        """
        Manage

        1. Make keyword like obj attr
        2. For keyword create request
        3. Pass request
        4. Parse it
        :return:
        """
        self.keyword = keyword

        request = self._create_request()

        content = self.pass_request(request)

        data = self.parse_content(content)

        return data


class DwParserSearch(AbstractSearchParser):

    url = 'https://www.dw.com/search/en?languageCode=en&origin=gN&item={}'

    base_url = 'https://www.dw.com'

    def _pagination(self):
        pass

    def _create_request(self) -> requests.PreparedRequest:
        url = self.url.format(self.keyword)
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

        # if self.is_paginate and depth < self.max_depth and data:
        #     content = self._pagination()
        return data


class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_search_parser(self):
        pass

    @abc.abstractmethod
    def create_top_parser(self):
        pass


class DwParsersFactory(AbstractFactory):

    def create_search_parser(self) -> AbstractSearchParser:
        return DwParserSearch()

    def create_top_parser(self):
        return DwParserTop()


# class BbcParsersFactory(AbstractFactory):
#     pass




#https://www.dw.com/search/en?searchNavigationId=9097&languageCode=en&origin=gN&item=nazi
#https://www.dw.com/search/en?languageCode=en&origin=gN&item=asd\