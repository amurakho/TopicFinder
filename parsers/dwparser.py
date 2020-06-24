import requests
import abc

from parsers._abcparser import Parser


class DwParserSearch(Parser):

    def __init__(self, search_fields: list):
        self.search_fields = search_fields

    def _create_request(self, keyword: str) -> requests.PreparedRequest:
        pass

    def parse_content(self, content: str) -> dict:
        pass

    def start_parse(self) -> dict:

        pass


class DwParserTop(Parser):

    def _create_request(self, keyword: str) -> requests.PreparedRequest:
        pass

    def parse_content(self, content: str) -> dict:
        pass

    def start_parse(self) -> dict:
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