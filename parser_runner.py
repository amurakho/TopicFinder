"""
Module which search all parsers files and create runner for each parser
"""
from const import PARSER_FOLDER_PATH, PATH
from pathlib import Path


def get_all_parsers_modules():
    parsers_modules = (PARSER_FOLDER_PATH.glob('*Parser.py'))


if __name__ == '__main__':
    get_all_parsers_modules()