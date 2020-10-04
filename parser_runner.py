"""
Module which search all parsers files and create runner for each parser
"""
import importlib
import pathlib

from db.sqlmanager import SqlManager
from const import PARSER_FOLDER, DB_SETTINGS


def get_all_parsers_modules():
    # file.parts[-1] -> get only filename
    # .split('.')[0] -> remove .pu
    # print(os.listdir(PARSER_FOLDER_PATH))

    files = [file.parts[-1].split('.')[0]
             for file in pathlib.Path(PARSER_FOLDER).glob('*Parser.py')]
    return files


def launch_search_parsers(factory, keywords):
    parser = factory.create_search_parser()

    data = []
    for keyword in keywords:
        data.extend(parser.start_parse(keyword))
    return data


def launch_top_parsers(factory):
    parser = factory.create_top_parser()
    data = parser.start_parse()
    return data


def save_to_base(data):
    manager = SqlManager(DB_SETTINGS)

    manager.add_to_base(data)


def print_stat(data):
    print(data[0])
    print(f'Scrapped count: {len(data)}')


def run_parsers(full_file_list, settings):
    files = settings['o'] if settings.get('o') else full_file_list
    for filename in files:
        filepath = '.'.join((PARSER_FOLDER, filename))
        mod = importlib.import_module(filepath)

        factory = mod.ParsersFactory()
        if not factory:
            continue
        if settings.get('k'):
            data = launch_search_parsers(factory, settings['k'])
        else:
            data = launch_top_parsers(factory)

        if settings.get('s'):
            save_to_base(data)

        print_stat(data)