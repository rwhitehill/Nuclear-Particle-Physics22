import pint
from scipy.constants import hbar,c,m_e

ureg = pint.UnitRegistry()
Q_   = ureg.Quantity

dx   = Q_(1e-13,'cm')
hbar = Q_(hbar,'J*s')
c    = Q_(c,'m/s')
m_e  = Q_(m_e,'kg')

p = (hbar/2/dx).to('kg*m/s')
print('{:~.1E}'.format(p.to('MeV/m*s')))

E2 = (p**2*c**2 + m_e**2*c**4).to('MeV**2')
E  = (E2)**0.5
print('{:~.1f}'.format(E.to('MeV')))

actual = Q_(0.019,'MeV')

print('%.1f'%(E/actual))

