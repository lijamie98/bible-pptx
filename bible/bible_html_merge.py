# -*- coding: utf-8 -*-
"""
Merge per-chapter HTML files into one plain text file per Bible book.
Reads from downloaded HTML (one file per chapter), strips formatting,
outputs one .txt file per book in New_Testament/ and Old_Testament/.
"""
import os
import re

from bible import BIBLE_HTML_PATH
from bible.bible_book_list import (
    new_testiment_book_list_traditional,
    old_testiment_book_list_traditional,
)

# Same naming as bible_html_downloader
FILE_FORMAT = '{0}_bible_Ch_{1}_.html'

# Output: data/html_merged/New_Testament/, data/html_merged/Old_Testament/
BIBLE_HTML_MERGED = os.path.join(os.path.dirname(BIBLE_HTML_PATH), 'html_merged')

# Verse row: <td ...><sup>N</sup>text</td>
VERSE_PATTERN = re.compile(r'<td[^>]*>\s*<sup>([^<]*)</sup>(.*?)</td>')


def get_chapter_html_path(html_folder, book_name, chapter):
    return os.path.join(html_folder, FILE_FORMAT.format(book_name, chapter))


def extract_verses_from_html(content):
    """Extract verse number and text from full-page HTML. Returns list of (num, text)."""
    verses = []
    for line in content.splitlines():
        m = VERSE_PATTERN.search(line)
        if m and m.group(1).strip().isdigit():
            num = m.group(1).strip()
            text = m.group(2).strip()
            verses.append((num, text))
    return verses


def merge_book(book, html_folder, out_folder):
    """
    Read all chapter HTML files for one book, extract plain content,
    write one merged plain text file for the book.
    """
    book_name = book['name']
    book_title = book.get('sk_title', book_name)
    chapters = book['chapters']

    parts = [book_title, '']

    for ch in range(1, chapters + 1):
        path = get_chapter_html_path(html_folder, book_name, ch)
        if not os.path.exists(path):
            print('  skip (missing): {0}'.format(path))
            continue
        with open(path, encoding='utf-8') as f:
            content = f.read()
        verses = extract_verses_from_html(content)
        parts.append('Chapter {0}'.format(ch))
        for num, text in verses:
            parts.append('{0} {1}'.format(num, text))
        parts.append('')

    os.makedirs(out_folder, exist_ok=True)
    out_path = os.path.join(out_folder, '{0}.txt'.format(book_name))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))
    print('Written: {0}'.format(out_path))


def main():
    nt_folder = os.path.join(BIBLE_HTML_PATH, 'New_Testament')
    ot_folder = os.path.join(BIBLE_HTML_PATH, 'Old_Testament')
    out_nt = os.path.join(BIBLE_HTML_MERGED, 'New_Testament')
    out_ot = os.path.join(BIBLE_HTML_MERGED, 'Old_Testament')

    print('Merging New Testament...')
    for book in new_testiment_book_list_traditional:
        merge_book(book, nt_folder, out_nt)

    print('Merging Old Testament...')
    for book in old_testiment_book_list_traditional:
        merge_book(book, ot_folder, out_ot)

    print('Done. Output in {0}'.format(BIBLE_HTML_MERGED))


if __name__ == '__main__':
    main()
