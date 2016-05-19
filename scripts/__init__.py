import os

BIBLE_SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

BIBLE_HOME = os.path.abspath(os.path.join(BIBLE_SCRIPT_PATH, os.pardir))
BIBLE_HTML_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "html"))
BIBLE_CSV_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "csv"))
BIBLE_PPTX_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "pptx"))
BIBLE_PPTX_TEMPLATE_PATH = os.path.abspath(os.path.join(BIBLE_HOME, "data", "templates"))

print "BIBLE_HOME={0}".format(BIBLE_HOME)
print "BIBLE_HTML_PATH={0}".format(BIBLE_HTML_PATH)
print "BIBLE_CSV_PATH={0}".format(BIBLE_CSV_PATH)
print "BIBLE_PPTX_PATH={0}".format(BIBLE_PPTX_PATH)
print "BIBLE_PPTX_TEMPLATE_PATH={0}".format(BIBLE_PPTX_TEMPLATE_PATH)

if not os.path.isdir(BIBLE_HTML_PATH):
    os.makedirs(BIBLE_HTML_PATH)

if not os.path.isdir(BIBLE_CSV_PATH):
    os.makedirs(BIBLE_CSV_PATH)

if not os.path.isdir(BIBLE_PPTX_PATH):
    os.makedirs(BIBLE_PPTX_PATH)

if not os.path.isdir(BIBLE_PPTX_TEMPLATE_PATH):
    os.makedirs(BIBLE_PPTX_TEMPLATE_PATH)
