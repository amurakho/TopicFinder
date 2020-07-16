# from const import KEYWORDS
# from parsers.dwparser import DwParsersFactory
#
# from parsers.tproggerparser import TproggerParser
#
# """
#     Main part - launch all
#
#     1) should use 'fabric method' to create different types of parsing objects
#
#
#     Need to create twitter/telegram parser
#         Twitter - by tags
#         Telegram - by channel
# """
#
# POLITICS_FABRICS = []
#
# PROGGER_FABRICS = []
#
#
# if __name__ == '__main__':
#     # parser = TproggerParser(['django'])
#     # data = parser.start_parse()
#     # print(data)
#     # pass
#     from const import POLITICS_KEYWORDS
#     fac = DwParsersFactory()
#     # p = fac.create_top_parser()
#     # data = p.start_parse()
#     # print(len(data))
#     # print(data)
#     p = fac.create_search_parser()
#     for keyword in POLITICS_KEYWORDS:
#         data = p.start_parse(keyword)
#         print(data)
#         break

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))
