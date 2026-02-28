import os
from . import bible_book_list

BIBLE_SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
BIBLE_HOME = os.path.abspath(os.path.join(BIBLE_SCRIPT_PATH, os.pardir))


class BibleContext:
    def __init__(self):
        self.theme = ""
        self.template_pptx_time = -1
        self.force_update = False
        pass

    def get_template_pptx(self):
        return os.path.join(self.template_path, '{0}.pptx'.format(self.theme))

    def get_csv_file_name(self, book, chapter):
        return os.path.join(self.csv_path, '{0}_{1}.csv'.format(book, chapter))

    def get_pptx_file_name(self, book, chapter):
        return os.path.join(self.pptx_path, self.theme, '{0}_{1:0>2d}.pptx'.format(book, chapter))

    def set_theme(self, theme):
        self.theme = theme
        self.template_pptx_time = os.path.getmtime(self.get_template_pptx())

        # Make sure the template output folder is set.
        template_output_folder = os.path.join(self.pptx_path, self.theme)

        if not os.path.isdir(template_output_folder):
            os.makedirs(template_output_folder)

    def to_be_updated(self, csv_file_name, pptx_file_name):
        if self.force_update:
            return True

        if not os.path.exists(pptx_file_name):
            return True

        pptx_time = os.path.getmtime(pptx_file_name)
        csv_time = os.path.getmtime(csv_file_name)

        if csv_time > pptx_time:
            return True

        if self.template_pptx_time > pptx_time:
            return True

        return False


class SimplifiedBibleContext(BibleContext):
    def __init__(self):
        BibleContext.__init__(self)
        self.csv_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "csv", "simplified"))
        self.pptx_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx", "simplified"))
        self.template_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates", "simplified"))
        self.new_testiment_book_list = bible_book_list.new_testiment_book_list_simplified
        self.old_testiment_book_list = bible_book_list.old_testiment_book_list_simplified


class TraditionalBibleContext(BibleContext):
    def __init__(self):
        BibleContext.__init__(self)
        self.csv_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "csv", "traditional"))
        self.pptx_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx", "traditional"))
        self.template_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates", "traditional"))
        self.new_testiment_book_list = bible_book_list.new_testiment_book_list_traditional
        self.old_testiment_book_list = bible_book_list.old_testiment_book_list_traditional


class ComboBibleContext(BibleContext):
    def __init__(self):
        BibleContext.__init__(self)
        self.csv_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "csv", "traditional"))
        self.pptx_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx_combo", "traditional"))
        self.template_path = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates_combo", "traditional"))
        self.new_testiment_book_list = bible_book_list.new_testiment_book_list_traditional
        self.old_testiment_book_list = bible_book_list.old_testiment_book_list_traditional


traditional_bible_context = TraditionalBibleContext()
simplified_bible_context = SimplifiedBibleContext()


def prepare_context(context):
    if not os.path.isdir(context.csv_path):
        os.makedirs(context.csv_path)
    if not os.path.isdir(context.pptx_path):
        os.makedirs(context.pptx_path)
    if not os.path.isdir(context.template_path):
        os.makedirs(context.template_path)


prepare_context(traditional_bible_context)
prepare_context(simplified_bible_context)

# The following is to be deprecated.
BIBLE_CSV_PATH_TRADITIONAL = os.path.abspath(os.path.join(BIBLE_HOME, "data", "csv", "traditional"))
BIBLE_CSV_PATH_SIMPLIFIED = os.path.abspath(os.path.join(BIBLE_HOME, "data", "csv", "simplified"))

BIBLE_PPTX_PATH_TRADITIONAL = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx", "traditional"))
BIBLE_PPTX_PATH_SIMPLIFIED = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx", "simplified"))

BIBLE_PPTX_TEMPLATE_PATH_TRADITIONAL = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates", "traditional"))
BIBLE_PPTX_TEMPLATE_PATH_SIMPLIFIED = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates", "simplified"))

BIBLE_HTML_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "html"))

BIBLE_COMBO_PPTX_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx_combo"))
BIBLE_COMBO_PPTX_TEMPLATE_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates_combo"))

BIBLE_DATABASE_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "text"))

# if not os.path.isdir(BIBLE_HTML_PATH):
#     os.makedirs(BIBLE_HTML_PATH)

# if not os.path.isdir(BIBLE_CSV_PATH_TRADITIONAL):
#     os.makedirs(BIBLE_CSV_PATH_TRADITIONAL)
#
# if not os.path.isdir(BIBLE_CSV_PATH_SIMPLIFIED):
#     os.makedirs(BIBLE_CSV_PATH_SIMPLIFIED)
#
# if not os.path.isdir(BIBLE_PPTX_PATH_TRADITIONAL):
#     os.makedirs(BIBLE_PPTX_PATH_TRADITIONAL)
#
# if not os.path.isdir(BIBLE_PPTX_PATH_SIMPLIFIED):
#     os.makedirs(BIBLE_PPTX_PATH_SIMPLIFIED)
#
# if not os.path.isdir(BIBLE_PPTX_TEMPLATE_PATH_TRADITIONAL):
#     os.makedirs(BIBLE_PPTX_TEMPLATE_PATH_TRADITIONAL)
