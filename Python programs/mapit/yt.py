#!/usr/bin/python

import webbrowser
import sys
open=webbrowser.open('https://www.youtube.com/results?search_query='+
                     '+'.join(sys.argv[1:]))
