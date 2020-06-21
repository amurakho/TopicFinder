import requests
import abc
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json

from errors import *


class Parser(abc.ABC):
    """
    Abstract parser class

    :param self.parser_name: Name of parser
    :param self.request_delay: Delay between requests
    :param self.url: url of parsed site
    """

    parser_name = None
    request_delay = 1
    request = None
    url = None
    search_url = None

    def __init__(self,  search_fields: list):
        """
        :param search_fields: field which will search(['Python', 'Django'])
        """
        self.search_fields = search_fields

    @abc.abstractmethod
    def _create_request(self, keyword: str) -> requests.PreparedRequest:
        """
        :param keyword: get a keyword for create request
        :param base_url: base url for search url creating

        Creating request to the site from self.url + self.search_field
        :return: Request obj(prepared)
        """
        pass

    def make_request(self, request: requests.PreparedRequest) -> str:
        """
        Pass request to the site
        :param request: Request obj
        :return:  Response obj
        """
        session = requests.Session()
        response = session.send(request)
        if response.status_code != 200:
            raise Not200RequesCode('Error with search request.'
                                   'Current code is: ', response.status_code)
        return response.content

    @abc.abstractmethod
    def parse_content(self, content: str) -> dict:
        """
        Parser manager of response

        :param content: content of response(html)
        :return: Parsed info in dict format
        """
        pass

    @abc.abstractmethod
    def manage(self) -> dict:
        """
        Loop each keyword in self.search_fields and launch full
        :return: dict with parsed info
        """
        pass



class HabrParser(Parser):
    pass


