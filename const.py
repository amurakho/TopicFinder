import pathlib

PROGRAMMING_SITES = {
    'tproger': 'https://tproger.ru/',
    'habr': 'https://habr.com/'
}

POLITICS_SITES = {
    'dw': 'https://www.dw.com',
    'cnn': 'https://edition.cnn.com/',
    'nationalrev': 'https://www.nationalreview.com/',
    'foxnews': 'https://www.foxnews.com/',
    'usnews': 'https://www.usnews.com',
    'independent': 'https://www.independent.co.uk',
    'spiegel': 'https://www.spiegel.de/international/',
    'upravda': 'https://www.pravda.com.ua/',
    'bbc': 'https://www.bbc.com',
    'scmp': 'https://www.scmp.com',
    'cgtn': 'https://www.cgtn.com/',
}

PROGRAMMING_KEYWORDS = ['python',  'django', ]

POLITICS_KEYWORDS = ['neo-nazi', 'nazi', 'fash', 'far-right', ]

KEYWORDS = {
    'politics': POLITICS_KEYWORDS,
    'programming': PROGRAMMING_KEYWORDS,
}

PATH = pathlib.Path(__file__).resolve().parent.parent

COMMANDS = (
    'run',
    'test',
)

HELP_TEXT = """
    COMMANDS : {}
""".format(COMMANDS)

TEST_FOLDER_PATH = PATH.joinpath('tests')

PARSER_FOLDER_PATH = PATH.joinpath('parsers')