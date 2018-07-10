#!/usr/bin/env python3

import os
import subprocess as sp
import json
import sys
words = {}
words[""] = ""

def load(filename):
    f = open(filename)
    tmp_words = json.loads(f.read())
    words.update(tmp_words)
    f.close()

directory = os.path.dirname(os.path.realpath(__file__))
for root, dirnames, filenames in os.walk("%s/dict"%(directory)):
    for filename in filenames:
        load('%s/dict/%s'%(directory, filename))

try:
    load('%s/extension.dict'%(directory))
except:
    pass
