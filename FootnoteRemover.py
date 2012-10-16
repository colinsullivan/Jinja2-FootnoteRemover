###
#   @file       FootnoteRemover.py
#
#   @author     Colin Sullivan <colinsul [at] gmail.com>
#
#               Copyright (c) 2012 Colin Sullivan
#               Licensed under the MIT license.
###


from jinja2.ext import Extension

from jinja2 import environmentfilter

from re import sub

@environmentfilter
def removefootnotes(env, value):
    """A basic jinja filter that removes markdown footnote
    definitions from text. Useful when outputting some
    section of a post as an excerpt and footnotes are
    not applicable."""

    if value:

        # Replace all "[^something]" strings with ""
        result = sub(r'\[\^[^\]]*\]', '', value)

        return result
    else:
        return value

class FootnoteRemover(Extension):
    
    tags = set(['removefootnotes'])

    def __init__(self, environment):
        environment.filters['removefootnotes'] = removefootnotes
        super(FootnoteRemover, self).__init__(environment)

    def parse(self, parser):
        pass
