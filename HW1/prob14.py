#!/usr/bin/env python3

import numpy as np
import pandas as pd
from itertools import combinations_with_replacement as cwr

import sys
sys.path.insert(0,'..')
from properties import *

q_info = quark().info
quarks = ['u','d','s','c']
baryons = list(cwr(quarks,3))

table = {'Baryon': [], 'charm': []}
for _ in baryons:
    baryon = ''.join(_)
    table['Baryon'].append(r'$%s$'%baryon)
    table['charm'].append('%.0f'%baryon.count('c'))

table = pd.DataFrame(table)
table.to_latex(buf='prob14.tex',
        index=False,
        escape=False,
        column_format='cc')
