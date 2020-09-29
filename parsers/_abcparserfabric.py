import abc
import requests

from errors import Not200RequesCode


class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_search_parser(self):
        pass

    @abc.abstractmethod
    def create_top_parser(self):
        pass


class AbstractTopParser(abc.ABC):

    url = ''

    @abc.abstractmethod
    def parse_content(self, content: bytes):
        pass

    def pass_request(self):
        response = requests.get(self.url)
        return response.content

    def start_parse(self):
        """
        Manage

        1. Create and pass request
        2. Parse data

        :return:
        """

        content = self.pass_request()

        data = self.parse_content(content)

        return data


class AbstractSearchParser(abc.ABC):
    """
    Interface for "search" parsers.

    """
    keyword = ''

    def __init__(self, is_paginate=False, max_depth=10):
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
