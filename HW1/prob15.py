#!/usr/bin/env python3

import numpy as np
import pandas as pd
from itertools import combinations_with_replacement as cwr

import sys
sys.path.insert(0,'..')
from properties import *

q_info = quark().info
quarks = ['u','d','s','c']
antiquarks = ['ub','db','sb','cb']

table = {'Meson': [], 'charm': []}
for q in quarks:
    for qb in antiquarks:
        table['Meson'].append(r'$%s\bar{%s}$'%(q,qb[0]))
        table['charm'].append((q=='c')-(qb=='cb'))

table = pd.DataFrame(table)
table.to_latex(buf='prob15.tex',
        index=False,
        escape=False,
        column_format='cc')
