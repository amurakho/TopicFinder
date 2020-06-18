import requests
import abc
from Parsers import Parser
import json


class Strategy(abc.ABC):

    @abc.abstractmethod
    def parse_response(self, content:str) -> dict:
        pass


class TproggerTagStrategy(Strategy):
    pass


class TproggerSearchStrategy(Strategy):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__strategy = None

    @property
    def strategy(self) -> Strategy:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        self.__strategy = strategy

    def parse_content(self, content: str) -> dict:
        return self.strategy.parse_response(content)
        # content = content.decode('utf-8')
        # start = content.find('{')
        # end = content.rfind('}') + 1
        # data = json.loads(content[start:end])
        # print(data)

    def manage(self):
        data = {}
        for keyword in self.search_fields:
            if keyword in self.tprogger_tags_list:
                self.strategy = TproggerTagStrategy()
                parsed_url = self.tprogger_tag_url
            else:
                self.strategy = TproggerSearchStrategy()
                parsed_url = self.search_url
            request = self._create_request(keyword, parsed_url)
            content = self.make_request(request)
            data[keyword] = self.parse_content(content)
            break
        return data