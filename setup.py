from os import listdir
import cgi, csv, json, email, parse
from optparse import OptionParser
# For web stuff: import sys, requests, string, secrets
import sys
targetIP = ""

import numpy as np
import virustotal_python

VERSION='0.01'
BUILD='Aug 29 2022'

FG_BLACK = 0x0000
FG_WHITE = 0xffff
FG_RED = 0x0001
FG_MAGENTA = 0x0005
FG_INTENSITY = 0x0008
COLOR_RESET = '\033[0m'  # Text Reset

def cprint(msg, color): 
    if color & FG_INTENSITY == FG_INTENSITY:
        color &= 0x7
        str_color = '\033[0;%2Xm' % (0x90 + color)
    else:
        str_color = '\033[0;%2Xm' % (0x30 + color)
        sys.stdout.write(str_color + msg + COLOR_RESET)
        sys.stdout.flush()

class OptionParsingError(RuntimeError):
    def __init__(self, msg):
        self.msg = msg


class OptionParsingExit(Exception):
    def __init__(self, status, msg):
        self.msg = msg
        self.status = status


class ModifiedOptionParser(OptionParser):
    def error(self, msg):
        raise OptionParsingError(msg)

    def exit(self, status=0, msg=None):
        raise OptionParsingExit(status, msg)

def options():
    usage = "Usage: %prog path[s] [options]"
    parser = ModifiedOptionParser(add_help_option=False, usage=usage)
    parser.add_option("-i", "--ip",
            action="store_true", dest="opt_files",
            default=True)
    parser.add_option("-t", "--toggle_brute",
            action="store_true", dest="opt_files",
            default=True)

    return parser


def main():
    cprint("Installing deps[*]\n", FG_MAGENTA)
    parser = options()

    if len(sys.argv) < 2:
        return 'NONE_OPTION', None
    else:
        try:
            (options, args) = parser.parse_args()
            if len(args) == 0:
                return options, None
        except (OptionParsingError, e): 
            return 'ILLEGAL_OPTION', e.msg
        except (OptionParsingExit, e):
            return 'ILLEGAL_OPTION', e.msg

if __name__ == "__main__":
    main()
