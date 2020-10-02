from parsers._abcparser import Parser


class HabrParser(Parser):

    def __init__(self, search_fields:list):
        self.search_fields = search_fields

    def parse_content(self, content: str):
        raise NotImplementedError('This method are not implemented')

    def _create_request(self, keyword: str):
        raise NotImplementedError('This method are not implemented')

    def start_parse(self):
        raise NotImplementedError('This parser are not implemented')


class ParsersFactory:

    def create_search_parser(self):
        raise NotImplemented

    def create_top_parser(self):
        raise NotImplemented
