# -*- coding: utf-8 -*-

import unicodedata

def stripList(tempList):
    t = tempList
    # if len(t) == 1:
        # logger.info('Only one item in the list. Skipping stripping.')
        # return t
    t = [x for x in t if x]
    t = map(lambda x: unicodedata.normalize('NFKD', x), t)
    t = map(lambda x: x.replace('\t', ''), t)
    t = map(lambda x: x.replace('\r', ''), t)
    t = map(lambda x: x.replace('\n', ''), t)
    t = map(lambda x: x.replace('&nbsp;', ''), t)
    t = map(lambda x: x.replace('&nbsp', ''), t)
    t = map(lambda s: s.strip(), t)
    t = map(lambda x: " ".join(x.split()), t)
    t = [it for it in t if it != '']
    return t
