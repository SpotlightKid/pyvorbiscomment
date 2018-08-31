#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Read and set comments in Ogg vorbis files."""

from __future__ import print_function, unicode_literals

import argparse
import logging
import sys

from mutagen.oggvorbis import OggVorbis


__version__ = '0.1.0'
log = logging.getLogger(__file__)


def parse_tag(tagstr):
    try:
        name, value = tagstr.split('=', 1)
    except ValueError:
        raise argparse.ArgumentTypeError('Could not parse comment tag (must be "name=value").')
    else:
        return name.strip().upper(), value.lstrip()


def create_argparser():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    list_group = ap.add_argument_group('Listing options')
    list_group.add_argument('-l', '--list', action="store_true",
                            help="List the comments (default if no options are given)")
    edit_group = ap.add_argument_group('Editing options')
    edit_group.add_argument('-a', '--append', action="store_true", help="Append comments")
    edit_group.add_argument('-t', '--tag', metavar="name=value", action="append", type=parse_tag,
                            help="Specify a comment tag on the commandline")
    edit_group.add_argument('-w', '--write', action="store_true",
                            help="Write comments, replacing the existing ones")
    misc_group = ap.add_argument_group('Miscellaneous options')
    misc_group.add_argument('-q', '--quiet', action="store_true",
                            help="Quiet mode. No messages are displayed")
    misc_group.add_argument('-V', '--version', action='version', version='%(prog)s ' + __version__)
    ap.add_argument('inputfile', help="Ogg Vorbis input file")
    ap.add_argument('outputfile', nargs='?', help="Output file (default: modify input file)")
    return ap


def parse_args(parser, args):
    args = args if args is not None else sys.argv[1:]
    if not args:
        raise ValueError("No input file.")

    return parser.parse_args(args)


def main(args=None):
    ap = create_argparser()
    try:
        args = parse_args(ap, args)
    except ValueError:
        parser.print_help(sys.stderr)
        return 2

    logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s",
        level=logging.WARNING if args.quiet else logging.INFO)

    oggfile = OggVorbis(args.inputfile)

    if args.write and args.tag:
        oggfile.tags.clear()

    for name, value in args.tag or []:
        if args.append:
            value = oggfile.tags[name.upper()] + [value]

        oggfile.tags[name.upper()] = value

    if args.write or args.append:
        oggfile.save(args.outputfile)

    if args.list or not any((args.tag, args.write, args.append)):
        for tag, value in sorted(oggfile.tags):
            print("{}: {}".format(tag, value))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
