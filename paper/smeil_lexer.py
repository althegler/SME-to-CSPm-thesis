import re
from pygments.lexer import RegexLexer
from pygments.token import *

class SMEILLexer(RegexLexer):
    name = 'SMEIL'
    aliases = ['smeil']
    filenames = ['*.sme']
    flags = re.IGNORECASE

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'//.*$', Comment.Single),

            (r'\b(as|barrier|break|bus|case|default|elif|else|enum|for|from|func|generate|if|import|instance|network|of|proc|range|return|simulation|switch|to|var|where|const)\b', Keyword.Reserved),
            (r'\b(sync|async|exposed|unique|len)\b', Keyword),
            (r'\b(trace)\b', Name.Builtin),
            (r'\b(true|false)\b', Keyword.Constant),

            (r'"', String.Double, 'string'),

            (r'==|<=|>=|!=|\*\*', Operator),
            (r'[=<>%&*+-/!]', Operator),

            (r'[+-]?\d+\.\d+', Number.Float),
            (r'[+-]?\d+', Number.Integer),

            (r'(?<=(:\s))(u?int|f32|f64|i\d+|u\d+|boolean)', Keyword.Type),

            (r'\.|,|:|;|\{|\}|\(|\)', Punctuation),

            (r'(?:[a-zA-Z][a-zA-Z0-9_-]*)', Name.Variable),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'(\{|\})', String.Interpol),
            (r'[^"\\\{\}]+', String),
        ]
    }
