import sys
import unittest
import logging
import argparse

import const
import errors

logging.basicConfig(level=logging.DEBUG)


class Commands:

    # def _parse_arguments(self, args, flags, parsed_args=None):
    #     arg = next(args)
    #
    #     if not parsed_args:
    #         parsed_args = list()
    #
    #     if arg.startswith('-') and arg not in flags.keys():
    #         print(f'Wrong "{arg}" flag with run command')
    #         return
    #
    #     elif arg.startswith('-') and arg in flags.keys():
    #         is_additional_args = flags[arg]['additional_args']
    #         parsed_args.append({
    #             'name': arg,
    #             'additional_args': [],
    #         })
    #
    #         if is_additional_args:
    #
    #             arg = next(args)
    #             while not arg.startswith('-'):
    #                 parsed_args[arg]['additional_args'].append(arg)
    #                 try:
    #                     arg.
    #     if args:

    def parse_arguments(self, flags):
        parser = argparse.ArgumentParser(prog='run', description='"run" command parse')
        parser.add_argument('run')
        parser.add_argument('-x', nargs='?')
        print(parser.parse_args())
        # args = sys.argv[2:]
        # flag_names = flags.keys()

    # def _parse_arguments2(self, flags):
    #     parsed_args = []
    #
    #     for arg in args:
    #         if arg.startswith('-') and arg not in flag_names:
    #             print(f'Wrong "{arg}" flag with run command')
    #
    #         elif arg.startswith('-') and arg in flag_names:
    #             is_additional_args = flags[arg]['additional_args']
    #
    #             add_list = []
    #             if is_additional_args:
    #
    #             d = {
    #                 'name': arg,
    #
    #             }

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
                'name': '-o',
                'description': 'Launch scrappers by name',
                'additional_args': True,
            },
            '-k': {
                'name': '-k',
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
