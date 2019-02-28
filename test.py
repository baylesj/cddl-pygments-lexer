#!/usr/bin/env python

from pygments.formatters.rtf import RtfFormatter
from pygments.lexers import load_lexer_from_file
from pygments import highlight

TEST_FILENAME = "osp_messages.cddl"
LEXER_FILENAME = "cddl_lexer.py"
OUTPUT_FILENAME = "test.rtf"

def main():
  lexer = load_lexer_from_file(LEXER_FILENAME)

  with open(TEST_FILENAME, 'r') as f:
    contents = f.read()

    formatter = RtfFormatter(style='monokai')

    return_val = highlight(contents, lexer, formatter)
    with open(OUTPUT_FILENAME, 'w') as f:
      f.write(return_val)


if __name__ == "__main__":
  main()