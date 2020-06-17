import abc

from const import PROGRAMMING_KEYWORDS
from Parsers import TproggerParser, Parser, HabrParser


class ScrapperFabric(abc.ABC):

    @abc.abstractmethod
    def create_parser(self, search_fields: list) -> Parser:
        pass


class TproggerParserFabric(ScrapperFabric):

    def create_parser(self, search_fields: list):
        return TproggerParser(search_fields=search_fields)


class HabrParserFabric(ScrapperFabric):

    def create_parser(self, search_fields: list):
        return HabrParser(search_fields=search_fields)


def launch_fabrics(site: str):
    fabric = None
    if site == 'tproger':
        fabric = TproggerParserFabric()
    elif site == 'habr':
        fabric = HabrParserFabric()
    else:
        return

    return fabric.create_parser(PROGRAMMING_KEYWORDS)