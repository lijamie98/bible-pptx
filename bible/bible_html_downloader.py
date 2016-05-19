import os

from bible_book_list import *
import urllib

from bible import BIBLE_HTML_PATH

url_format = 'http://www.ccreadbible.org/Chinese%20Bible/sigao/{0}_bible_Ch_{1}_.html'
file_format = '{0}_bible_Ch_{1}_.html'


def get_download_url(book, chapter):
    return url_format.format(book, chapter)


def get_file_name(folder, book, chapter):
    return os.path.join(folder, file_format.format(book, chapter))


def download_book_list(book_list, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for book in book_list:
        for chapter in range(1, book['chapters'] + 1):
            url = get_download_url(book['name'], chapter)
            file_name = get_file_name(folder, book['name'], chapter)
            if not os.path.exists(file_name):
                print 'downloading from {0} to {1}...'.format(url, file_name)
                urllib.urlretrieve(url, file_name)


if __name__ == "__main__":
    download_book_list(new_testiment_book_list, os.path.join(BIBLE_HTML_PATH, 'New_Testament'))
    download_book_list(old_testiment_book_list, os.path.join(BIBLE_HTML_PATH, 'Old_Testament'))
