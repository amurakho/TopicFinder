import abc

from const import PROGRAMMING_KEYWORDS
from parsers._abcparser import Parser
from parsers.habrparser import HabrParser
from parsers.tproggerparser import TproggerParser


class ScrapperFabric(abc.ABC):

    @abc.abstractmethod
    def create_parser(self, search_fields: list) -> Parser:
        pass


class EmptyFabric(ScrapperFabric):
    """
    Just empty fabric

    Code in launch_fabrics are clearly with this class
    """

    def create_parser(self, search_fields: list):
        raise NotImplementedError('Wrong site name')


class TproggerParserFabric(ScrapperFabric):

    def create_parser(self, search_fields: list):
        return TproggerParser(search_fields=search_fields)


class HabrParserFabric(ScrapperFabric):

    def create_parser(self, search_fields: list):
        return HabrParser(search_fields=search_fields)


def launch_fabrics(site: str):
    if site == 'tproger':
        fabric = TproggerParserFabric()
    elif site == 'habr':
        fabric = HabrParserFabric()
    else:
        fabric = EmptyFabric()

    return fabric.create_parser(PROGRAMMING_KEYWORDS)


if __name__ == '__main__':
    parser = launch_fabrics('tproger')
    parser.start_parse()


