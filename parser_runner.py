"""
Module which search all parsers files and create runner for each parser
"""
import importlib
import pathlib

from const import PARSER_FOLDER


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
    pass


def print_stat(data):
    print(data[0])
    print(f'Scrapped count: {len(data)}')


def run(file_list, settigns):
    print(settigns)
    # for filename in file_list:
    #     filepath = '.'.join((PARSER_FOLDER, filename))
    #     mod = importlib.import_module(filepath)
    #
    #     factory = mod.ParsersFactory()
    #     if not factory:
    #         continue
    #
    #     if settigns.get('k'):
    #         data = launch_search_parsers(factory, keywords)
    #     else:
    #         data = launch_top_parsers(factory)
    #
    #     if settigns.get('s'):
    #         save_to_base(data)
    #
    #     print_stat(data)


def main():
    file_list = get_all_parsers_modules()
    run(file_list)

if __name__ == '__main__':
    main()