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

    def _create_request(self, keyword: str, base_url: str) -> requests.PreparedRequest:
        """
        :param keyword: get a keyword for create request
        :param base_url: base url for search url creating

        Creating request to the site from self.url + self.search_field
        :return: Request obj
        """
        url = base_url.format(keyword)
        return requests.Request(url=url, method='GET').prepare()

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
    def parse_response(self, content: str) -> dict:
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


class TproggerParser(Parser):

    parser_name = 'tproger.ru parser'
    url = 'https://tproger.ru/'
    search_url = 'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=ru&source=gcsc' \
                 '&gss=.ru&cselibv=57975621473fd078&cx=partner-pub-9189593931769509:9105321070&q={}' \
                 '&safe=off&cse_tok=AJvRUv0i_A115uJUfuYZUeCUD7Rw:1592494068316&exp=csqr,cc,' \
                 '4355059&callback=google.search.cse.api5275'
    tprogger_tag_url = 'https://tproger.ru/tag/{}/'
    tprogger_tags_list = ['python', 'javascript', 'go', 'java', 'cpp', 'c-sharp', 'php',
                          'css', 'sql']

    def parse_response(self, content: str) -> dict:
        content = content.decode('utf-8')
        start = content.find('{')
        end = content.rfind('}') + 1
        data = json.loads(content[start:end])
        print(data)

    def create_request(self, keyword: str) -> requests.PreparedRequest:
        if keyword in self.tprogger_tags_list:
            return self._create_request(keyword, self.tprogger_tag_url)
        else:
            return self._create_request(keyword, self.search_url)

    def manage(self):
        data = {}
        for keyword in self.search_fields:
            request = self.create_request(keyword)
            response = self.make_request(request)
            data[keyword] = self.parse_response(response)
            break
        return data

class HabrParser(Parser):
    pass


