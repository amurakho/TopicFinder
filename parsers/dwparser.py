import requests
import abc
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

    def __init__(self, search_fields: list, is_paginate=True, max_depth=10):
        self.search_fields = search_fields
        self.is_paginate = is_paginate
        self.max_depth = max_depth

    @abc.abstractmethod
    def _create_request(self, keyword):
        pass

    @abc.abstractmethod
    def parse_content(self, content):
        pass

    @abc.abstractmethod
    def _pagination(self):
        pass

    def pass_request(self, request: requests.PreparedRequest) -> bytes:
        session = requests.Session()
        response = session.send(request)
        if response.status_code != 200:
            raise Not200RequesCode('Error with search request.'
                                   'Current code is: ', response.status_code)
        return response.content

    def start_parse(self):
        data = {}
        for keyword in self.search_fields:

            request = self._create_request(keyword)

            content = self.pass_request(request)
            print(content[:100])
            # data[keyword] = self.parse_content(content)
            break


class DwParserSearch(AbstractSearchParser):

    url = 'https://www.dw.com/search/en?languageCode=en&origin=gN&item={}'

    def _create_request(self, keyword: str) -> requests.PreparedRequest:
        url = self.url.format(keyword)
        return requests.Request(url=url, method='GET').prepare()

    def parse_content(self, content):
        pass



class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_search_parser(self, search_fields):
        pass

    @abc.abstractmethod
    def create_top_parser(self):
        pass


class DwParsersFactory(AbstractFactory):

    def create_search_parser(self, search_fields: list) -> Parser:
        return DwParserSearch(search_fields)

    def create_top_parser(self):
        return DwParserTop()



# class BbcParsersFactory(AbstractFactory):
#     pass


#https://www.dw.com/search/en?searchNavigationId=9097&languageCode=en&origin=gN&item=nazi
#https://www.dw.com/search/en?languageCode=en&origin=gN&item=asd\