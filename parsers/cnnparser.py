from bs4 import BeautifulSoup

from const import POLITICS_SITES
from parsers._abcparserfabric import AbstractFactory, AbstractSearchParser, AbstractTopParser


CNN_BASE_URL = POLITICS_SITES.get('cnn')


class CnnParserTop(AbstractTopParser):

    url = 'https://edition.cnn.com/'
    
    def parse_content(self, content: bytes):
        soup = BeautifulSoup(content, 'lxml')
        data = []
        
        blocks = soup.find_all('d')
    
    def parse_blocks(self, blocks, data):
        pass

class CnnParserSearch(AbstractSearchParser):
    pass
    #cd__headline


class DwParsersFactory(AbstractFactory):

    def create_search_parser(self) -> AbstractSearchParser:
        return CnnParserSearch()

    def create_top_parser(self) -> AbstractTopParser:
        return CnnParserTop()