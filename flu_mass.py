# % ------------------------------
# % filename: flu_mass.m
# %
# % used to compute the mass matrix
# ie is
# vcore is
def function flu_mass(ie,vcore):
	x   = vcore[1 ,:] - vcore[0,:]
	xl  = sqrt(x * x' )
	vme = xl./6.*[ 2 1 
    1 2];
return vme

if __name__ == '__main__':
	flu_mass()