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

def lol(needle,haystack): # list of lists :)
    """Wählt aus einer Liste von Listen diejenige aus, deren Kopf der 'needle' entspricht"""
    for N in haystack:
        print N
        if needle == N[0]:
            return N
    return None

def add_again(new_again, time_new):
    """Fügt einen Eintrag hinzu."""
    old_agains_reader = csv.reader(open(dotagain,'rb')) # erstmal holen wir uns die alten Einträge
    # bastelt eine Liste aus allen agains:
    old_agains = []
    for row in old_agains_reader:
        old_agains.append(row[0])
    # falls wir new_again schon haben, kommt die Zeit hinten ran:
    H = lol(new_again, old_agains_reader)
    if H:
        H.append(time_new)
    # sonst erstellen wir eine neue Liste
    else:
        H = [new_again, time_new]
    print H

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
    pass

if __name__ == '__main__':
    if not os.path.exists(dotagain):
        print "\'~/.again\' existiert nicht. Ich werd\'s anlegen."
        open(dotagain,'w').close()
    dispatch()
