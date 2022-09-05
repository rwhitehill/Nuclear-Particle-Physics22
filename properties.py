#!/usr/bin/env python3

class quark:

    def __init__(self):
        self.info = {}

        self.info['u'] = {}
        self.info['u']['Q']    = +2/3
        self.info['u']['m'] = 2.4    # MeV
        self.info['u']['S'] = 0
        
        self.info['d'] = {}
        self.info['d']['Q']    = -1/3
        self.info['d']['m'] = 4.8    # MeV
        self.info['d']['S'] = 0

        self.info['c'] = {}
        self.info['c']['Q']    = 2/3
        self.info['c']['m'] = 1.27e3 # MeV
        self.info['c']['S'] = 0

        self.info['s'] = {}
        self.info['s']['Q']    = -1/3
        self.info['s']['m'] = 104    # MeV
        self.info['s']['S'] = -1

        for q in list(self.info.keys()):
            self.info[q+'b'] = {}
            self.info[q+'b']['Q'] = -self.info[q]['Q']
            self.info[q+'b']['m'] = self.info[q]['m']
            self.info[q+'b']['S'] = -self.info[q]['S']


class lepton:
    
    def __init__(self):
        self.info = {}
        
        self.info['e'] = {}
        self.info['e']['Q'] = -1
        self.info['e']['m'] = 0.511 # MeV

class meson_octet(quark):

    def __init__(self):
        super().__init__()

        self.info = {}

        self.info['pi(+)'] = {}
        self.info['pi(+)']['m'] = 139.57039 # MeV 
        self.info['pi(+)']['valence'] = ['u','db']
        self.info['pi(+)']['Q'] = +1 
        self.info['pi(+)']['S'] = 0 

        self.info['pi(-)'] = {}
        self.info['pi(-)']['m'] = 139.57039 # MeV 
        self.info['pi(-)']['valence'] = ['d','ub']
        self.info['pi(-)']['Q'] = -1
        self.info['pi(-)']['S'] = 0 

        self.info['pi(0)'] = {}
        self.info['pi(0)']['m'] = 134.9768 # MeV
        self.info['pi(0)']['valence1'] = ['u','ub']
        self.info['pi(0)']['valence2'] = ['d','db']
        self.info['pi(0)']['Q'] = 0
        self.info['pi(0)']['S'] = 0

        self.info['eta'] = {}
        self.info['eta']['m'] = 547.862 # MeV
        self.info['eta']['valence1'] = ['s','sb']
        self.info['eta']['valence2'] = ['u','ub']
        self.info['eta']['valence3'] = ['d','db']
        self.info['eta']['Q'] = 0
        self.info['eta']['S'] = 0

        self.info['K(-)'] = {}
        self.info['K(-)']['m'] = 493.677 # MeV
        self.info['K(-)']['valence'] = ['s','ub']
        self.info['K(-)']['Q'] = -1
        self.info['K(-)']['S'] = -1

        self.info['K(+)'] = {}
        self.info['K(+)']['m'] = 493.677 # MeV
        self.info['K(+)']['valence'] = ['u','sb']
        self.info['K(+)']['Q'] = +1
        self.info['K(+)']['S'] = +1

        self.info['K(0)'] = {}
        self.info['K(0)']['m'] = 497.611
        self.info['K(0)']['valence'] = ['d','sb']
        self.info['K(0)']['Q'] = 0
        self.info['K(0)']['S'] = 1

        self.info['Kb(0)'] = {}
        self.info['Kb(0)']['m'] = 497.611
        self.info['Kb(0)']['valence'] = ['s','db']
        self.info['Kb(0)']['Q'] = 0
        self.info['Kb(0)']['S'] = -1


class baryon_octet(quark):
    
    def __init__(self):
        super().__init__()

        self.info = {}

        self.info['p'] = {}
        self.info['p']['m']       = 938.27208816 # Mev
        self.info['p']['valence'] = ['u','u','d']
        self.info['p']['Q'] = +1 
        self.info['p']['S'] = 0


        self.info['n'] = {}
        self.info['n']['m']       = 939.5654205 # MeV
        self.info['n']['valence'] = ['u','d','d']
        self.info['n']['Q'] = 0
        self.info['n']['S'] = 0

        self.info['Lambda^{0}'] = {}
        self.info['Lambda^{0}']['m'] = 1115.683 # MeV
        self.info['Lambda^{0}']['valence'] = ['u','d','s']
        self.info['Lambda^{0}']['Q'] = 0 
        self.info['Lambda^{0}']['S'] = -1 

        self.info['Sigma^{+}'] = {}
        self.info['Sigma^{+}']['m'] = 1189.37 # MeV
        self.info['Sigma^{+}']['valence'] = ['u','u','s']
        self.info['Sigma^{+}']['Q'] = 1
        self.info['Sigma^{+}']['S'] = -1

        self.info['Sigma^{-}'] = {}
        self.info['Sigma^{-}']['m'] = 1197.449 # MeV
        self.info['Sigma^{-}']['valence'] = ['d','d','s']
        self.info['Sigma^{-}']['Q'] = -1
        self.info['Sigma^{-}']['S'] = -1

        self.info['Sigma^{0}'] = {}
        self.info['Sigma^{0}']['m'] = 1192.642 # MeV 
        self.info['Sigma^{0}']['valence'] = ['u','d','s']
        self.info['Sigma^{0}']['Q'] = 0
        self.info['Sigma^{0}']['S'] = -1

        self.info['Xi^{-}'] = {}
        self.info['Xi^{-}']['m'] = 1321.71 # MeV
        self.info['Xi^{-}']['valence'] = ['d','s','s']
        self.info['Xi^{-}']['Q'] = -1
        self.info['Xi^{-}']['S'] = -2

        self.info['Xi^{0}'] = {}
        self.info['Xi^{0}']['m'] = 1314.86 # MeV
        self.info['Xi^{0}']['valence'] = ['u','s','s']
        self.info['Xi^{0}']['Q'] = 0
        self.info['Xi^{0}']['S'] = -2

class baryon_decuplet(quark):
    
    def __init__(self):
        super().__init__()

        self.info = {}

        self.info['Omega^{-}'] = {}
        self.info['Omega^{-}']['m'] = 1672.45 # MeV
        self.info['Omega^{-}']['valence'] = ['s','s','s']
        self.info['Omega^{-}']['Q'] = -1
        self.info['Omega^{-}']['S'] = -3

        self.info['Xi^{*0}'] = {}
        self.info['Xi^{*0}']['m'] = 1531.80 # MeV
        self.info['Xi^{*0}']['valence'] = ['u','s','s']
        self.info['Xi^{*0}']['Q'] = 0
        self.info['Xi^{*0}']['S'] = -2

        self.info['Xi^{*-}'] = {}
        self.info['Xi^{*-}']['m'] = 1535.0
        self.info['Xi^{*-}']['valence'] = ['d','s','s']
        self.info['Xi^{*-}']['Q'] = -1
        self.info['Xi^{*-}']['S'] = -2

        self.info['Sigma^{*+}'] = {}
        self.info['Sigma^{*+}']['m'] = 1382.8 # MeV
        self.info['Sigma^{*+}']['valence'] = ['u','u','s']
        self.info['Sigma^{*+}']['Q'] = +1
        self.info['Sigma^{*+}']['S'] = -1

        self.info['Sigma^{*0}'] = {}
        self.info['Sigma^{*0}']['m'] = 1383.7 # MeV
        self.info['Sigma^{*0}']['valence'] = ['u','d','s']
        self.info['Sigma^{*0}']['Q'] = 0
        self.info['Sigma^{*0}']['S'] = -1

        self.info['Sigma^{*-}'] = {}
        self.info['Sigma^{*-}']['m'] = 1387.2 # MeV
        self.info['Sigma^{*-}']['valence'] = ['d','d','s']
        self.info['Sigma^{*-}']['Q'] = -1
        self.info['Sigma^{*-}']['S'] = -1

        self.info['Delta^{-}'] = {}
        self.info['Delta^{-}']['m'] = 1232 # MeV 
        self.info['Delta^{-}']['valence'] = ['d','d','d']
        self.info['Delta^{-}']['Q'] = -1
        self.info['Delta^{-}']['S'] = 0 

        self.info['Delta^{0}'] = {}
        self.info['Delta^{0}']['m'] = 1232 # MeV 
        self.info['Delta^{0}']['valence'] = ['u','d','d']
        self.info['Delta^{0}']['Q'] = 0 
        self.info['Delta^{0}']['S'] = 0 

        self.info['Delta^{+}'] = {}
        self.info['Delta^{+}']['m'] = 1232 # MeV 
        self.info['Delta^{+}']['valence'] = ['u','u','d']
        self.info['Delta^{+}']['Q'] = +1 
        self.info['Delta^{+}']['S'] = 0 

        self.info['Delta^{++}'] = {}
        self.info['Delta^{++}']['m'] = 1232 # MeV
        self.info['Delta^{++}']['valence'] = ['u','u','u']
        self.info['Delta^{++}']['Q'] = +2 
        self.info['Delta^{++}']['S'] = 0 


if __name__ == '__main__':
    pass


