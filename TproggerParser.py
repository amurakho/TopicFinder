import requests
import abc
from abstractParser import Parser
import json
import time


class Strategy(abc.ABC):
    parsed_url = ''
    keyword = ''


    @abc.abstractmethod
    def parse_response(self, content:str) -> dict:
        pass

    @abc.abstractmethod
    def create_request(self, keyword: str) -> requests.PreparedRequest:
        pass


class TproggerTagStrategy(Strategy):
    parsed_url = 'https://tproger.ru/tag/{}/'

    def parse_response(self, content: str):
        print(content)


class TproggerSearchStrategy(Strategy):
    """
    Strategy when i need parse page from tags

    Note: tporgger use google service for search. And google api
    use some cookie - cse_token for auth the site.
    So, before search rqeust i must take this cse_token.
    And i take it in get_cse_token method.
    """

    parsed_url = 'https://cse.google.com/cse/element/v1?rsz=filtered_cse&' \
                 'num={num}' \
                 '&hl=ru&source=gcsc&gss=.ru' \
                 '&start={start}' \
                 '&cselibv=57975621473fd078&cx=partner-pub-9189593931769509:9105321070' \
                 '&q=python&safe=off&' \
                 'cse_tok={cse}' \
                 '&exp=csqr,cc,' \
                 '4355059&callback=google.search.cse.api10582'

    def __init__(self, keyword: str, is_paginate=False, per_page=20, max_depth=10):
        """
        :param keyword: searching word
        :param is_paginate: if need paginate
        :param per_page: result per page(20 is ok)
        :param max_depth: if paginate, how deeper needed parse

        cse_token: token for auth and pass search request to google
        """
        self.data = []
        self.is_paginate = is_paginate
        self.per_page = per_page
        self.keyword = keyword
        self.max_depth = max_depth
        self.cse_token = ''

    def parse_json_to_dict(self, content: dict):
        """
        Format getting data to dict data
        :param content: parsed data

        :return if page are empty - False else - True
        """
        results = content.get('results')
        if not results:
            return False
        for res in results:
            t = {
                'title': res.get('titleNoFormatting'),
                'text': res.get('title'),
                'url': res.get('formattedUrl'),
                'pub_date': res.get('richSnippet', {}).get('article', {}).get('datepublished')
            }
            self.data.append(t)
        return True

    def _pagination(self):
        """
            Send request with new data to paginate and return new response
        :return: Response of new page
        """
        url = self.parsed_url.format(num=20, start=20, keyword=self.keyword, cse=self.cse_token)
        result = requests.get(url=url)
        return result.content

    @staticmethod
    def _decode_content(content: bytes):
        """
        Get json part and decode if
        :return: decoded content
        """
        content = content.decode('utf-8')
        start = content.find('{')
        end = content.rfind('}') + 1
        content = json.loads(content[start:end])
        return content

    def parse_response(self, content: bytes, depth=0):
        """
        Scrape and format to dict
        """
        content = self._decode_content(content)
        # parse_json_to_dict meth are try to get data from content
        # and if it exist - return True, else - False.
        not_empty = self.parse_json_to_dict(content)
        print('Here')
        if self.is_paginate and not_empty and depth < self.max_depth:
            content = self._pagination()
            time.sleep(60)
            self.parse_response(content, depth=depth+1)
        else:
            return self.data

    @staticmethod
    def get_cse_token():
        """
        Pass request to google for the cse_token
        :return: cse_token
        """
        cse_url = 'https://cse.google.com/cse.js?cx=partner-pub-9189593931769509:9105321070'
        response = requests.get(url=cse_url).content.decode('utf-8')
        # first split - i make cse_token value at start of the last element of the list
        response = response.split('"cse_token":')[-1]
        # second split - by comma so cse_token value will be in first element of the list
        token = response.split(',')[0].strip()
        return token[1:-1]

    def create_request(self, keyword: str) -> requests.PreparedRequest:
        self.cse_token = self.get_cse_token()
        url = self.parsed_url.format(keyword=keyword, num=20, start=0, cse=self.cse_token)
        return requests.Request(url=url, method='GET').prepare()


class TproggerParser(Parser):

    parser_name = 'tproger.ru parser'
    url = 'https://tproger.ru/'
    tprogger_tags_list = ['python', 'javascript', 'go', 'java', 'cpp', 'c-sharp', 'php',
                          'css', 'sql']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__strategy = None

    @property
    def strategy(self) -> Strategy:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy_arg):
        self.__strategy = strategy_arg

    def parse_content(self, content: str) -> dict:
        return self.strategy.parse_response(content)

    def _create_request(self, keyword: str) -> requests.PreparedRequest:
        return self.strategy.create_request(keyword)

    def manage(self):
        data = {}
        for keyword in self.search_fields:
            # choose strategy
            if keyword in self.tprogger_tags_list:
                self.strategy = TproggerTagStrategy(keyword=keyword)
            else:
                self.strategy = TproggerSearchStrategy(keyword=keyword)
            # create request
            request = self._create_request(keyword)
            content = self.make_request(request)
            data[keyword] = self.parse_content(content)
            break
        print(data)
        return data