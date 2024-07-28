# Before starting, open the CEDICT text file and delete the copyright information at the top. Otherwise the program will try to parse it and you will get an error message.
# Characters that are commonly used as surnames have two entries in CC-CEDICT. This program will remove the surname entry if there is another entry for the character. If you want to include the surnames, simply delete lines 59 and 60.
# Written by Franki Allegra in February 2020. Adapted by Patrick Hu in July 2024.
import os
import json


def parse_line(line):
    # Sample entry.
    # 鼠標 鼠标 [shu3 biao1] /mouse (computing)/
    # 亞太區 亚太区 [Ya4 Tai4 qu1] /Asian area/the Far East/Asia Pacific region/
    parsed = {}
    if line == '':
        dict_lines.remove(line)
        return 0
    line = line.rstrip('/')
    line = line.split('/')  # Split each gloss.
    # first gloss contains traditional simplified then pinyin
    # second gloss contains main english translation
    # subsequent glosses contain supplementary english translations
    if len(line) <= 1:
        return 0
    english = line[1:]
    char_and_pinyin = line[0].split('[')
    characters = char_and_pinyin[0]
    # characters goes from a list of 1 string to a list of 2 strings, traditional and simplified
    characters = characters.split()
    traditional = characters[0]
    simplified = characters[1]
    pinyin = char_and_pinyin[1]
    pinyin = pinyin.rstrip().rstrip(']')
    parsed['traditional'] = traditional
    parsed['simplified'] = simplified
    parsed['pinyin'] = pinyin
    parsed['english'] = english  # english will be a list of all the glosses
    list_of_dicts.append(parsed)


def remove_surnames():
    for x in range(len(list_of_dicts)-1, -1, -1):
        if 'surname' in list_of_dicts[x]['english']:
            if list_of_dicts[x]['traditional'] == list_of_dicts[x+1]['traditional']:
                list_of_dicts.pop(x)


def main():
    print("Parsing dictionary...")
    for line in dict_lines:
        parse_line(line)
    remove_surnames()
    return list_of_dicts


# Open CEDICT file.
# Get the directory of the current script.
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file.
file_path = os.path.join(script_dir, 'cedict_ts.u8')
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    lines = text.split('\n')
    dict_lines = list(lines)

list_of_dicts = []
parsed_dict = main()

# Write to a JSON file.
# Already ran.
# file_path = os.path.join(script_dir, 'parsed_dict.json')
# with open(file_path, 'w', encoding='utf-8') as file: # BE CAREFUL OF THE CWD NOT BEING SET PROPERLY
#     json.dump(parsed_dict, file, ensure_ascii=False, indent=2)

# __name__ = "__main__":
# when a module is being imported, its __name__ attribute will be set to the name of the module itself
# But when the module is being run directly as a script such as python module.py, then __name__ is set to "__main__"
# So this idiom checks whether a module is being imported or run directly.

# Each time a change is made to the Django's project files, the watcher detects and restarts the server automatically.
