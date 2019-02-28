from pygments.lexer import RegexLexer
from pygments.token import *

class CustomLexer(RegexLexer):
    name = 'CDDL'
    aliases = ['cddl']
    filenames = ['*.cddl']

    tokens = {
        'root': [
            #(r'[a-zA-Z0-9-.$@]+:', Name.Label),
            #(r'[a-zA-Z0-9-.$@]+', Name),
            (r' +', Whitespace),
            (r'[#=?:&({})/[\]*]', Operator),
            #(r':', Operator, "keyValuePair"),
            (r'[,]', Punctuation),
            (r';.*?$', Comment.Singleline),
            (r'(uint)', Keyword.Type),
            #(r'/', Text)
        ],
        #'keyValuePair': [
        #  (r'[0-9]+$', Number),
        #]
        #,
        #'object': [
        #  (r'[({]', Punctuation, '#push'),
        #  (r'[})]', Punctuation, '#pop')
        #]
#        'comment': [
#            (r'[^*/]', Comment.Multiline),
#            (r'/\*', Comment.Multiline, '#push'),
#            (r'\*/', Comment.Multiline, '#pop'),
#            (r'[*/]', Comment.Multiline)
#        ]
    }