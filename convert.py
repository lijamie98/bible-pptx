# -*- coding: utf-8 -*-
import argparse
import csv
import os

from pptx import Presentation

from bible import BIBLE_CSV_PATH, BIBLE_PPTX_PATH, BIBLE_PPTX_TEMPLATE_PATH
from bible.bible_book_list import new_testiment_book_list, old_testiment_book_list

__theme__ = 'simple'

# Default force_update mode to False.
__force_update__ = False

max_verse = -1


def get_csv_file_name(book, chapter):
    return os.path.join(BIBLE_CSV_PATH, '{0}_{1}.csv'.format(book, chapter))


def get_pptx_file_name(book, chapter):
    return os.path.join(BIBLE_PPTX_PATH, __theme__, '{0}_{1:0>2d}.pptx'.format(book, chapter))


def to_be_updated(csv_file_name, pptx_file_name):
    if __force_update__:
        return True

    if not os.path.exists(pptx_file_name):
        return True

    pptx_time = os.path.getmtime(pptx_file_name)
    csv_time = os.path.getmtime(csv_file_name)

    if csv_time > pptx_time:
        return True

    return False


def parse_csv_file(book_name, book_title, chapter):
    csv_file_name = get_csv_file_name(book_name, chapter)
    pptx_file_name = get_pptx_file_name(book_name, chapter)

    if not to_be_updated(csv_file_name, pptx_file_name):
        # Skip
        return

    prs = Presentation(os.path.join(BIBLE_PPTX_TEMPLATE_PATH, '{0}.pptx'.format(__theme__)))

    title_slide_layout_large = prs.slide_layouts[0]
    title_slide_layout_medium = prs.slide_layouts[1]
    title_slide_layout_small = prs.slide_layouts[2]
    title_slide_layout_extra_small = prs.slide_layouts[3]

    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            verse_content = row[3]

            if len(verse_content) <= 150:  # 10 x 5
                slide = prs.slides.add_slide(title_slide_layout_large)
            elif len(verse_content) <= 216:  # 72 = 12 x 6
                slide = prs.slides.add_slide(title_slide_layout_medium)
            elif len(verse_content) <= 360:  # 72 = 15 x 8
                slide = prs.slides.add_slide(title_slide_layout_small)
            else:  # 18 x 10
                slide = prs.slides.add_slide(title_slide_layout_extra_small)

            title = slide.shapes.title
            subtitle = slide.placeholders[1]

            title.text = u'{0} - [{1}:{2}]'.format(book_title, row[1], row[2])
            subtitle.text = row[3]
            # print "{0} {1}:{2} {3}".format(row[0], row[1], row[2], row[3])

    print "Creating {0}".format(pptx_file_name)
    prs.save(pptx_file_name)


def parse_csv_files(book_list):
    for book in book_list:
        for chapter in range(1, book['chapters'] + 1):
            parse_csv_file(book['name'], book['title'], chapter)


def convert():
    theme_path = os.path.join(BIBLE_PPTX_PATH, __theme__)

    if not os.path.isdir(theme_path):
        os.makedirs(theme_path)

    parse_csv_files(new_testiment_book_list)
    parse_csv_files(old_testiment_book_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", help="The pptx template theme. ")
    parser.add_argument("--force", help="Force update all PPTX files.", nargs='*')
    args = parser.parse_args()

    if args.theme is None:
        __all__ = True
    else:
        __all__ = False
        __theme__ = args.theme

    if args.force is None:
        __force_update__ = False
    else:
        __force_update__ = True

    if __all__:
        for theme_file in os.listdir(BIBLE_PPTX_TEMPLATE_PATH):
            if theme_file.endswith(".pptx"):
                __theme__ = theme_file[0:-5]
                convert()
    else:
        convert()
