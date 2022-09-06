import sys
sys.path.insert(0,'..')
from properties import baryon_octet

bo = baryon_octet().info

# ['p', 'n', 'Lambda^{0}', 'Sigma^{+}', 'Sigma^{-}', 'Sigma^{0}', 'Xi^{-}', 'Xi^{0}']
baryons = list(bo.keys())

N   = baryons[:2]
Xi  = baryons[6:8]
Sig = baryons[3:6]

m_N   = sum(bo[_]['m'] for _ in N)/2
m_Xi  = sum(bo[_]['m'] for _ in Xi)/2
m_Sig = sum(bo[_]['m'] for _ in Sig)/3

print('%.0f'%m_N)
print('%.0f'%m_Xi)
print('%.0f'%m_Sig)

m_Lam = (2*(m_N+m_Xi)-m_Sig)/3
print('%.0f'%m_Lam)

print('%.1f'%(bo['Lambda^{0}']['m']/m_Lam))

