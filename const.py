import pathlib
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')


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
}

PROGRAMMING_KEYWORDS = ['python',  'django', ]

POLITICS_KEYWORDS = []

KEYWORDS = {
    'politics': POLITICS_KEYWORDS,
    'programming': PROGRAMMING_KEYWORDS,
}

PATH = pathlib.Path(__file__).resolve().parent

COMMANDS = (
    'run',
    'test',
)

HELP_TEXT = """
    COMMANDS : {}
""".format(COMMANDS)

TEST_FOLDER_PATH = 'tests'

PARSER_FOLDER = 'parsers'

DB_FOLDER = 'db'

DB_SETTINGS = {
    'drivername': 'postgresql',
    'database': config['DB']['name'],
    'username': config['DB']['user'],
    'password': config['DB']['password'],
    'host': config['DB']['host'],
    'port': config['DB']['port'],
}