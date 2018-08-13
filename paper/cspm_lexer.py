## Adapted from https://github.com/jnwhiteh/pygments_csp_lexer/blob/master/csp_lexer/__init__.py
from pygments.lexer import RegexLexer, bygroups, using, this
from pygments.token import *

class CSPmLexer(RegexLexer):
    name = "CSPm"
    aliases = ["cspm"]
    filenames = ["*.cspm"]

    tokens = {
        'root': [
            # comments
            (r'{-', Comment.Multiline, 'comment'),
            ('--.*$', Comment.Single),

            # whitespace
            (r'\s+', Text),

            (r'\[(FD|T|F)=', Keyword.Pseudo),
            (r'\\|->|\[\]|\|~\||\|\|\||\[\||\|]|\[\[|\]\]|\|\|', Operator),
            (r'{\||\|}|\.\.|<-|<->|==|<=|>=', Operator),
            (r'[{}:#@&=+-/*%^<>?!]', Operator),
            (r'\b(assert|datatype|let|within|newtype|channel|external|transparent)\b', Keyword.Reserved),
            (r'\b(if|then|else)\b', Keyword),
            (r'\b(\d+)\b', Number.Integer),
            (r'\b(true|false|True|False)\b', Keyword.Constant),
            (r'\b(length|null|head|tail|concat|elem|union|inter|diff|Union|Inter|member|card|empty|set|seq|Int|Bool|Proc|Events|STOP|SKIP|CHAOS|prioritise|productions|extensions|diamond|normal|sbisim|tau_loop_factor|model_compress|explicate|wbisim|chase)\b', Name.Builtin),
            (r'\(|\)|,|\[|\]', Punctuation),
            (r'^(\s*)([a-zA-Z0-9_\']+)(\s*)(\(.*?\)|)(\s*=)', bygroups(Text, Name.Function, Text, using(this), Text)),
            (r'[A-Za-z_][A-Za-z0-9_\']*', Name),
        ],
        'comment': [
            # Multiline Comments
            (r'[^-{}]+', Comment.Multiline),
            (r'{-', Comment.Multiline, '#push'),
            (r'-}', Comment.Multiline, '#pop'),
            (r'[-{}]', Comment.Multiline),
        ],
    }
