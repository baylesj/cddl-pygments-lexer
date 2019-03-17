#!/usr/bin/env python

import os

from pygments.formatters.html import HtmlFormatter
from pygments.lexers import load_lexer_from_file
from pygments import highlight

TEST_FILENAME = "osp_messages.cddl"
LEXER_FILENAME = "cddl_lexer.py"

def pygmentize_file(lexer, filename):
  print("Reading file from: {}".format(filename))
  with open(filename, 'r') as f:
    contents = f.read()

  formatter = HtmlFormatter(style='monokai', cssfile='style.css')

  return_val = highlight(contents, lexer, formatter)
  output_filename = "{}.html".format(os.path.splitext(filename)[0])

  with open(output_filename, 'w') as f:
    print("Pygmentizing output to: {}".format(output_filename))
    f.write(return_val)


def pygmentize_dir(lexer):
  for filename in os.listdir("."):
    if filename.endswith(".cddl"):
      pygmentize_file(lexer, filename)

if __name__ == "__main__":
  lexer = load_lexer_from_file(LEXER_FILENAME)
  pygmentize_dir(lexer)
