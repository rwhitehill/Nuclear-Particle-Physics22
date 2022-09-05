import sys
sys.path.insert(0,'../')
from properties import *


bd = baryon_decuplet().info
bo = baryon_octet().info
mo = meson_octet().info

particles = ['Delta(-)','Sigma*(+)','Xi*(-)']

print('(a)',end='\n')
for particle in particles:
    for baryon in bo.keys():
        for meson in mo.keys():
            Q_cond = bd[particle]['Q'] - (bo[baryon]['Q'] + mo[meson]['Q']) == 0
            S_cond = bd[particle]['S'] - (bo[baryon]['S'] + mo[meson]['S']) == 0

            if Q_cond and S_cond:
                print('%s --> %s + %s'%(particle,baryon,meson))
    print()

print(2*'\n')
print('(b)')
for particle in particles:
    for baryon in bo.keys():
        for meson in mo.keys():
            Q_cond = bd[particle]['Q'] - (bo[baryon]['Q'] + mo[meson]['Q']) == 0
            S_cond = bd[particle]['S'] - (bo[baryon]['S'] + mo[meson]['S']) == 0
            M_cond = bd[particle]['m'] - (bo[baryon]['m'] + mo[meson]['m']) >= 0

            if Q_cond and S_cond and M_cond:
                print('%s --> %s + %s'%(particle,baryon,meson))
    print()


