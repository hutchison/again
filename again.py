#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import sys
import os
import datetime
import csv

dotagain = os.path.expanduser('~/.again')

def list_agains():
    """Listet alle Einträge."""
    agains = csv.reader(open(dotagain,'rb'))
    print "Bisherige Einträge:"
    for row in agains:
        print row[0] + ":", ",".join(row[1:])

def add_again(new_again, time_new):
    """Fügt einen Eintrag hinzu."""
    old_agains = csv.reader(open(dotagain,'rb'))
    print "Debug (add_again):", old_agains
    print new_again, time_new
    # TODO: einen Eintrag auch wirklich hinzufügen (sollte doch eigentlich nicht so schwer sein)

def dispatch():
    """Entscheidet was zu tun ist."""
    if len(sys.argv) == 1:
        list_agains()
    else:
        new_a = " ".join(sys.argv[1:])  # alle übergebenen Strings werden zu einem zusammengefasst
                                        # so wird aus ['Wäsche', 'waschen'] auch 'Wäsche waschen'
        t = datetime.datetime.now()
        add_again(new_a, t)
        # TODO: Meldung machen!

def main():
    homedir = os.path.expanduser('~')
    againWriter = csv.writer(open(dotagain,'wb'))
    againWriter.writerow(sys.argv)

if __name__ == '__main__':
    try:
        f = open(dotagain,'rwb')
        f.close()
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    dispatch()
