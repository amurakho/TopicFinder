import sys
import unittest
import logging

import const
import errors

logging.basicConfig(level=logging.DEBUG)


class Commands:

    def _parse_command(self):
        args = sys.argv[2:]
        parsed_args = []

        for arg in args:

            print(arg)

    def test(self):
        suite = unittest.TestLoader().discover(str(const.TEST_FOLDER_PATH))
        unittest.TextTestRunner(verbosity=2).run(suite)

    def run(self):
        self._parse_command()


def main():
    if len(sys.argv) == 1:
        print(const.HELP_TEXT)
        exit(1)

    handler = getattr(Commands(), sys.argv[1], errors.UnknownCommand())
    return handler()


if __name__ == '__main__':
    main()
