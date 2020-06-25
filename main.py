from const import KEYWORDS
from parsers.dwparser import DwParsersFactory

"""
    Main part - launch all

    1) should use 'fabric method' to create different types of parsing objects
    
    
    Need to create twitter/telegram parser
        Twitter - by tags
        Telegram - by channel
"""

POLITICS_FABRICS = []

PROGGER_FABRICS = []


if __name__ == '__main__':
    from const import POLITICS_KEYWORDS
    fac = DwParsersFactory()
    p = fac.create_search_parser()
    for keyword in POLITICS_KEYWORDS:
        data = p.start_parse(keyword)
        print(data)
        break