#!/usr/bin/env python3
import sys
sys.path.insert(0,'..')
from properties import baryon_octet
import pandas as pd

m = {'u':336,'d':336,'s':540}
m_bind = -62

bo = baryon_octet().info 

table = {'Baryon ($qqq$)': [],
         'Calculated Mass (\qty{}{\MeV})': [],
         'Percent Error from PDG': []}

table_keys = list(table.keys())
for baryon in bo.keys():
    table[table_keys[0]].append(r'$%s%s~(%s)$'%('\\' if baryon not in ['p','n'] else '',baryon,''.join(bo[baryon]['valence'])))

    temp = sum([m[_] for _ in bo[baryon]['valence']]) + m_bind
    err  = (temp - bo[baryon]['m'])/bo[baryon]['m']*100

    table[table_keys[1]].append('%.0f'%temp)
    table[table_keys[2]].append(r'%.2f\%%'%err)

table = pd.DataFrame(table)
table.to_latex(buf='prob17.tex',
        index=False,
        escape=False,
        column_format='ccc')
