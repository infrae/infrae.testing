# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from BeautifulSoup import BeautifulSoup
from optparse import OptionParser
import sys

def xmlindent():
    """Indent an XML file.

    Can be used in emacs on your buffer with C-x h C-u M-S | path to
    the script Enter.
    """
    parser = OptionParser()
    (options, files) = parser.parse_args()

    if not files:
        input = ''
        data = sys.stdin.read()
        while data:
            input += data
            data = sys.stdin.read()
        print BeautifulSoup(input).prettify()
        return

    for filename in files:
        with open(filename, 'r') as input:
            print BeautifulSoup(input.read()).prettify()