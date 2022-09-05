#!/usr/bin/env python3

import numpy as np
import pandas as pd
from itertools import combinations_with_replacement as cwr

# properties: [charge,up,down,strange,charm]
quarks = {'u': np.array([ 2/3,1,0, 0,0]),
          'd': np.array([-1/3,0,1, 0,0]),
          's': np.array([-1/3,0,0,-1,0]),
          'c': np.array([ 2/3,0,0, 0,1])}
antiquarks = {r'\bar{u}': np.array([-2/3,-1, 0,0, 0]),
              r'\bar{d}': np.array([ 1/3, 0,-1,0, 0]),
              r'\bar{s}': np.array([ 1/3, 0, 0,1, 0]),
              r'\bar{c}': np.array([-2/3, 0, 0,0,-1])}

done = []
for q in quarks.keys():
    for qb in antiquarks.keys(): 
        comb = {q,qb}
        if comb not in done: 
            done.append(comb)
            props = quarks[q] + antiquarks[qb]
            print(r'${}{}$ & {:.0f} & {:.0f} & {:.0f} & {:.0f} & {:.0f} \\'.format(q,qb,*props))

