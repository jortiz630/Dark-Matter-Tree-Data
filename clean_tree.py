import numpy as np
from scipy import integrate
from scipy import interpolate
import random as random
import copy
###################################
h = 0.67
filename = "tree_3mpc.dat"
data = open(filename, "r").readlines()
data = data[44:]

#get snapshot scale factors                                                                                
counter = 0
scales = []
for l in data:
    if l.startswith("#"):
        counter=counter+1
    if counter > 1:
        break
    if not l.startswith("#"):
        parts = l.split()
        if len(scales) == 0:
            scales.append(float(parts[0]))
        if float(parts[0]) != scales[-1]:
            scales.append(float(parts[0]))
scales.reverse()

outname = "./scales_3mpc.dat"
f = open(outname, 'w')
for a in scales:
    print a
    f.write('%5.5f \n' % a)
f.close()


#    if ia == 3:
#        break
outname = "./trees_3mpc_clean.dat"
f = open(outname, 'w')
for (nl,l) in enumerate(data):
        if not l.startswith("#"):
            f.write(l)
f.close()
