import sys
import unittest
import logging
import argparse

import const
import errors
from parser_runner import get_all_parsers_modules

logging.basicConfig(level=logging.DEBUG)


class Commands:

    def parse_arguments(self, flags):
        parser = argparse.ArgumentParser(prog='run', description='"run" command parse')
        parser.add_argument('run')
        for flag, data in flags.items():
            action = 'append' if data['additional_args'] else 'store_true'
            if data.get('choices'):
                parser.add_argument(flag, action=action, choices=data.get('choices'))
            else:
                parser.add_argument(flag, action=action)

        return vars(parser.parse_args())

    def test(self):
        suite = unittest.TestLoader().discover(str(const.TEST_FOLDER_PATH))
        unittest.TextTestRunner(verbosity=2).run(suite)

    def run(self):
        flags = {
            '-s': {
                'description': 'Save to db',
                'additional_args': False,
            },
            '-o': {
                'description': 'Launch scrappers by name',
                'additional_args': True,
                'choices': [*get_all_parsers_modules()]
            },
            '-k': {
                'description': 'Launch with keywords',
                'additional_args': True
            },
        }

        self.parse_arguments(flags)


def main():
    if len(sys.argv) == 1:
        print(const.HELP_TEXT)
        exit(1)

    handler = getattr(Commands(), sys.argv[1], errors.UnknownCommand())
    return handler()


if __name__ == '__main__':
    main()
