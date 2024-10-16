import os
import json
from .models import Word


script_dir = os.path.dirname(os.path.abspath(__file__))


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


def remove_variants():
    for x in range(len(list_of_dicts)-1, -1, -1):
        if 'variant' in list_of_dicts[x]['english'][0]:
            # print(list_of_dicts[x]['english'])
            # Remove from db.
            Word.objects.filter(
                english=list_of_dicts[x]['english']).delete()
            list_of_dicts.pop(x)


def remove_dupes():
    # Removes dupes from db.
    for row in Word.objects.all().reverse():
        if Word.objects.filter(simplified=row.simplified).count() > 1:
            print(row.simplified + " was deleted")
            row.delete()


def main():
    for line in dict_lines:
        parse_line(line)
    remove_surnames()
    remove_variants()


print("Loading JSON file.")
path = os.path.join(script_dir, 'parsed_dict.json')
with open(path, 'r') as f:
    parsed_dict = json.load(f)
print(parsed_dict[0])
Word.objects.all().delete()


# print("Parsing dictionary.")
# path = os.path.join(script_dir, 'cedict_ts.u8')
# with open(path, 'r', encoding='utf-8') as file:
#     text = file.read()
#     lines = text.split('\n')
#     dict_lines = list(lines)
# list_of_dicts = []
# main()
# print("Done.")

print("Saving to database (this may take a few minutes) . . .")
for one_dict in parsed_dict:
    new_word = Word(traditional=one_dict["traditional"], simplified=one_dict["simplified"],
                    english=one_dict["english"], pinyin=one_dict["pinyin"])
    new_word.save()
print("Done.")

# print("Writing to JSON file.")
# path = os.path.join(script_dir, 'parsed_dict.json')
# with open(path, 'w', encoding='utf-8') as file:
#     json.dump(list_of_dicts, file, ensure_ascii=False, indent=2)
# print("Done.")

# __name__ = "__main__":
# when a module is being imported, its __name__ attribute will be set to the name of the module itself
# But when the module is being run directly as a script such as python module.py, then __name__ is set to "__main__"
# So this idiom checks whether a module is being imported or run directly.


# Each time a change is made to the Django's project files, the watcher detects and restarts the server automatically.


# If you want to save to a database as JSON objects, create a class Word in the Models file of your Django project:
# print("Saving to database (this may take a few minutes) . . .")
# for one_dict in list_of_dicts:
#     new_word = Word(traditional = one_dict["traditional"], simplified = one_dict["simplified"], english = one_dict["english"], pinyin = one_dict["pinyin"])
#     new_word.save()
