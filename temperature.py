def temperature(C_v,vsol):
    vtemp=(vsol[:,2]/vsol[:,0]-0.5*vsol[:,1]**2/vsol[:,0]**2)/C_v
    return vtemp 