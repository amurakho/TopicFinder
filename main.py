from const import KEYWORDS
# from parsers.dwParser import DwParsersFactory
from parsers.tproggerParser import TproggerParser

from db import sqlmanager
"""
    Main part - launch all

    1) should use 'fabric method' to create different types of parsing objects


    Need to create twitter/telegram parser
        Twitter - by tags
        Telegram - by channel
"""

POLITICS_FABRICS = []

PROGGER_FABRICS = []


# if __name__ == '__main__':
