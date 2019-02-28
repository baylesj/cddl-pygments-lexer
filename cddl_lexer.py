import re

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

# Based on draft spec here:
# https://tools.ietf.org/html/draft-ietf-cbor-cddl-05#section-3
class CustomLexer(RegexLexer):
    name = 'CDDL'
    aliases = ['cddl']
    filenames = ['*.cddl']

    flags = re.MULTILINE | re.UNICODE

    tokens = {
        'root': [
            (r'\n', Text),
            (r'[\-\_\@\.\$\s]+', Text),
            (r'\\\n', Text),  # line continuations
            (r';[^\n]*\n', Comment.Single),
            (r'(var|func|struct|map|chan|type|interface|const)\b',
             Keyword.Declaration),
            (words((
                'break', 'default', 'select', 'case', 'defer', 'go',
                'else', 'goto', 'switch', 'fallthrough', 'if', 'range',
                'continue', 'for', 'return'), suffix=r'\b'),
             Keyword),

            (r'(true|false|null|nil)\b', Keyword.Constant),

            (words((
                'uint', 'nint', 'int',
                'float16', 'float32', 'float64',
                'bstr', 'tstr'
                ), suffix=r'\b(\()'),
             bygroups(Name.Builtin, Punctuation)),
            (words((
                'uint', 'nint', 'int',
                'float16', 'float32', 'float64',
                'bstr', 'tstr'
                ), suffix=r'\b'),
             Keyword.Type),

            # Representation type
            (r'#[0-7](\.\d+)?', Keyword.Type),

            # imaginary_lit
            (r'\d+i', Number),
            (r'\d+\.\d*([Ee][-+]\d+)?i', Number),
            (r'\.\d+([Ee][-+]\d+)?i', Number),
            (r'\d+[Ee][-+]\d+i', Number),
            # float_lit
            (r'\d+(\.\d+[eE][+\-]?\d+|'
             r'\.\d*|[eE][+\-]?\d+)', Number.Float),
            (r'\.\d+([eE][+\-]?\d+)?', Number.Float),
            # int_lit
            # -- octal_lit
            (r'0[0-7]+', Number.Oct),
            # -- hex_lit
            (r'0[xX][0-9a-fA-F]+', Number.Hex),
            # -- decimal_lit
            (r'(0|[1-9][0-9]*)', Number.Integer),
            # char_lit
            (r"""'(\\['"\\abfnrtv]|\\x[0-9a-fA-F]{2}|\\[0-7]{1,3}"""
             r"""|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|[^\\])'""",
             String.Char),
            # StringLiteral
            # -- raw_string_lit
            (r'`[^`]*`', String),
            # -- interpreted_string_lit
            (r'"(\\\\|\\"|[^"])*"', String),
            # Tokens
            (r'(<<=|>>=|<<|>>|<=|>=|&\^=|&\^|\+=|-=|\*=|/=|%=|&=|\|=|&&|\|\|'
             r'|<-|\+\+|--|==|!=|:=|\.\.\.|[+\-*/%&])', Operator),
            (r'#', Keyword.Constant),
            (r'[|^<>=!?()\[\]{}.,:]', Punctuation),
            # identifier
            (r'[^\W\d]\w*', Name.Other),
        ]
    }