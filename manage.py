import sys
import unittest

import const
import errors


class Commands:

    def test(self):
        suite = unittest.TestLoader().discover(str(const.TEST_FOLDER_PATH))
        unittest.TextTestRunner(verbosity=2).run(suite)


    def run(self):
        print('RUN')
        pass


def main():
    if len(sys.argv) == 1:
        print(const.HELP_TEXT)
        exit(1)

    handler = getattr(Commands(), sys.argv[1], errors.UnknownCommand())
    return handler()


if __name__ == '__main__':
    main()
