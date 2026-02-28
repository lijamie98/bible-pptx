import re
import os

from bible import BIBLE_HTML_PATH
from bible.bible_book_list import *
from bible import BIBLE_CSV_PATH_TRADITIONAL

file_format = '{0}_bible_Ch_{1}_.html'


def get_html_file(html_path, book, chapter):
    return os.path.join(html_path, file_format.format(book, chapter))


def get_csv_file(book, chapter):
    return os.path.join(BIBLE_CSV_PATH_TRADITIONAL, '{0}_{1}.csv'.format(book, chapter))


def parse_file(book_name, chapter, html_file, csv_file):
    print("parsing {0} and writing to {1}".format(html_file, csv_file))
    with open(csv_file, 'w', encoding='utf-8') as f_csv:
        with open(html_file, encoding='utf-8') as f:
            content = f.readlines()
            for line in content:
                # Match verse lines: <td ...><sup>N</sup>verse text</td>
                verse_match = re.search(r'<td[^>]*>\s*<sup>([^<]*)</sup>(.*?)</td>', line)
                if verse_match:
                    verse_number = verse_match.group(1).strip()
                    verse_text = verse_match.group(2).strip()
                    if verse_number.isdigit():  # skip e.g. Plone<sup>®</sup>
                        f_csv.write('{0},{1},{2},{3}\n'.format(book_name, chapter, verse_number, verse_text))


def parse_files(book_list, html_path):
    for book in book_list:
        for chapter in range(1, book['chapters'] + 1):
            html_file = get_html_file(html_path, book['name'], chapter)
            csv_file = get_csv_file(book['name'], chapter)
            parse_file(book['name'], chapter, html_file, csv_file)


if __name__ == "__main__":
    parse_files(new_testiment_book_list_traditional, os.path.join(BIBLE_HTML_PATH, 'New_Testament'))
    parse_files(old_testiment_book_list_traditional, os.path.join(BIBLE_HTML_PATH, 'Old_Testament'))
    # parse_files(test_list, 'c:\\bible\\src\\Test\\')
