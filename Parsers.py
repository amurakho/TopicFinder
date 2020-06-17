import requests
import abc
import asyncio
import aiohttp


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
    def _create_request(self) -> requests.Request:
        """
        Creating request to the site from self.url + self.search_field
        :return: Request obj
        """
        pass

    @abc.abstractmethod
    def make_request(self, request: requests.Request) -> requests.Response:
        """
        Pass request to the site
        :param request: Request obj

        :return:  Response obj
        """
        pass

    @abc.abstractmethod
    def parse_response(self, response: requests.Response) -> dict:
        """
        Parser manager of response

        :param response:  Response obj
        :return: Parsed info in dict format
        """
        pass

    def manage(self) -> dict:
        """
        Loop each keyword in self.search_fields and launch full
        :return: dict with parsed info
        """
        for keyword in self.search_fields:



class TproggerParser(Parser):

    parser_name = 'tproger.ru parser'
    url = 'https://tproger.ru/'
    search_url = 'https://tproger.ru/search/?q='

    def _create_request(self):
        # self.search_url +=
        pass

    def mana

class HabrParser(Parser):
    pass