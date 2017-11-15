# % ---------------------------------
# % filename: initialize_data_structure.py
# %
# % we set the physical data of the structure.
# %============================================================
# % physical data of the structure
# %===========================================================
import numpy as np
from initialize_data_fluid import *
vprel=np.zeros((2,1))
vprel[0] = 1e7  #% spring rigidity
vprel[1]= 100  #% mass of the piston
Lsp0     = 1.2  #% length of the spring (unstretched)
Lspe     = Lsp0-(pres_init0-p_ext)*A/vprel[0] #% length at equilibrium

if(Lspe<=0):
    print(1,'Length of the spring at equilibrium Lspe= %g! meters ! \n',Le)
    


# % ----------------------------------
# % We compute the natural period of the (mass+spring) system
# %
omega0 = np.sqrt(vprel[0]/vprel[1]) #% natural pulsation
freq0  = omega0/(2*np.pi)       #% natural frequency
T0     = 1/freq0                #% natural period
#%
print(1,'Piston mass= %g kg \n',vprel[1])
print(1,'Spring rigidity= %g N/m \n',vprel[0])
print(1,'Natural frequency of the mass-spring system= %g Hz \n\n',freq0)

# % ============================================================
# % Data initialization for the structure
# % ===========================================================
# % beware of the sign of U0
# % u_t is the current displacement of the piston set to the initial displacement
# % u_dot_t  is the current velocity of the piston
# % u_double_dot_t  is the current acceleration of the piston
# %
u_t     = U0
u_dot_t = 0
vsols0  = u_t
# %
# % ------------------------
# % initialization of the acceleration
vfg0             = (vpres[nnt-1]-0*pres_init)*A
u_double_dot_t   = (vfg0+vprel[0]*(Lspe - u_t - Lsp0))/vprel[1]
