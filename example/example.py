#!/usr/bin/env python
#coding=utf-8
#file: example.py
"""
Example
"""



def example_function(param):
    """
    Example function.

    Keyword arguments:
    param -- the return value

    """
    return param


def main():
    parser = OptionParser()
    #parser.add_option("-f","--file",dest="filename",help="write report to FILE",metavar="FILE")
    #parser.add_option("-d","--date",dest="date",help="published DATE",metavar="DATE")
    parser.add_option("-v", action="store_true", dest="verbose", default=False, help="print status messages to stdout")

    (options,args) = parser.parse_args()
    if len(args) == 0:
        param = ""
    else:
        param = args[0]
    example_function(param)


if __name__ == "__main__":
    main()
