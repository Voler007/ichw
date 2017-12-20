#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Feiyang Xu"
__pkuid__  = "1700011742"
__email__  = "1700011742@pku.edu.cn"
"""

import sys
import urllib.request
from urllib.request import urlopen 



def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    c=""
    for i in lines:
        if ord(i)>=97 and ord(i)<=122:
            c=c+i
        elif ord(i)>=65 and ord(i)<=90:
            c=c+i
        else:
            c=c+" "

    d=c.split()
    l=len(d)
    e=[]
    f=[]
    for i in range(l):
        if d[i] not in e:
            e.append(d[i])
            f.append(1)
        else:
            g=e.index(d[i])
            f[g]=f[g]+1
    for j in range(topn):
        m=max(f)
        n=f.index(m)
        print(e[n],"\t",f[n])
        del e[n]
        del f[n]
    pass


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
