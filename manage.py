import sys
import unittest
import logging
import argparse

import const
import errors
from parser_runner import get_all_parsers_modules, run

logging.basicConfig(level=logging.DEBUG)


def parse_add_list(string):
    data = string.split(' ')
    return data


class Commands:

    def test(self):
        suite = unittest.TestLoader().discover(str(const.TEST_FOLDER_PATH))
        unittest.TextTestRunner(verbosity=2).run(suite)

    def run(self):
        files = get_all_parsers_modules()

        parser = argparse.ArgumentParser(prog='run', description='"run" command parse')
        parser.add_argument('run')
        parser.add_argument('-s', action='store_true')
        parser.add_argument('-o', action='append', choices=files)
        parser.add_argument('-k', type=parse_add_list)

        settings = vars(parser.parse_args())

        run(files, settings)


def main():
    if len(sys.argv) == 1:
        print(const.HELP_TEXT)
        exit(1)

    handler = getattr(Commands(), sys.argv[1], errors.UnknownCommand())
    return handler()


if __name__ == '__main__':
    main()
