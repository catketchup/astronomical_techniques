import numpy.random as random
import numpy as np

def simncoins(ncoins,nsims):
    rolls=random.rand(nsims,ncoins)
    headnum=np.sum(rolls[:,:]>0.5,axis=1)
    return headnum
    