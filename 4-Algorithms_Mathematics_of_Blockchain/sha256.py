#!/bin/python

import sys

inputM = sys.argv[1]

print("Msg: ", inputM)

Msg = ""
for c in inputM:
    Msg+= "{0:{fill}8b}".format(ord(c), fill='0')
    print(c, "{0:{fill}8b}".format(ord(c), fill='0'))

l = len(Msg)

Msg+='1'

k = 512 - (l+1) - 64

for i in rnage(0, k):
    Msg += '0'

Msg += "{0:{fill64b}".format(l, fill='0')

MsgList = []
tmpStr = ""
i = 1
for c in Msg:
