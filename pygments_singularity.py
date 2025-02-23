from pygments.lexer import RegexLexer, bygroups, using, words
from pygments.token import *
from pygments.lexers.shell import BashLexer
import re

class SingularityLexer(RegexLexer):
    """
    Lexer for pages in Singularity Admin Guide at https://www.apptainer.org/admin-docs/\{adminversion\}/
    """

    name = 'Singularity'
    aliases = ['singularity']
    filenames = ['*.def', 'Singularity']
    flags = re.IGNORECASE | re.MULTILINE | re.DOTALL

    _headers = r'^(\s)*(bootstrap|from|osversion|mirrorurl|include|registry|namespace|includecmd)(:)'
    _section = r'^%(?:pre|post|setup|environment|help|labels|test|runscript|files|startscript)\b'
    _appsect = r'^%app(?:install|help|run|labels|env|test|files)\b'

    tokens = {
        'root': [
            (_section, Generic.Heading, 'script'),
            (_appsect, Generic.Heading, 'script'),
            (_headers, bygroups(Text, Keyword, Text)),
            (r'\s*#.*?\n', Comment),
            (r'\b(([0-9]+\.?[0-9]*)|(\.[0-9]+))\b', Number),
            (r'(?!^\s*%).', Text),
        ],
        'script': [
            (r'(.+?(?=^\s*%))|(.*)', using(BashLexer), '#pop'),
        ],
    }
