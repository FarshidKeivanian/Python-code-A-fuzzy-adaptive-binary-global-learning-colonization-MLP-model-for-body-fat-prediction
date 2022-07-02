# -*- coding: utf-8 -*-
"""
Spyder Editor

This is the python version of the code.
"""
#Variables and expressions in Python (Spyder)
import numpy as np

# Probability of applying Velocity Divergence    
PVD = 1

# Probability of applying Velocity Adaptation
PVA = 1

nVar = 13
VarSize = np.arange(1,nVar+1)
VarMin = -1
VarMax = 1

VelMax = 1
VelMin = -1

GlobalMin = 0
# Parameters
MaxIt = 100
nPop = 20
nEmp = 5
mu = 0.05
alpha = 1            # Selection Pressure
Beta = 1
pRevolution = 0.1
zeta = 0.1           # Colonies Mean Cost Coefficient
nCol = nPop - nEmp

pDivergence = 0.1
n = 3
q = 3
VTR = 1e-4
w=1              # Inertia Weight
wdamp=0.99         # Inertia Weight Damping Ratio
c1=2               # Global Learning Coefficient
c2=2               # Personal Learning Coefficient

beta_min=0   # Lower Bound of Scaling Factor
beta_max=1   # Upper Bound of Scaling Factor

# Initialisation
class struct:
    pass
empty_country = struct()
empty_country.Position=[]
empty_country.Velocity=[]
empty_country.Cost=[]
empty_country.Out=[]

empty_country.Best = struct()
empty_country.Best.Position=[]
empty_country.Best.Cost=[]
empty_country.Best.Out=[]

class struct:
    pass
country = struct()
country = np.matlib.repmat(empty_country, nPop, 1)


GlobalBest = struct()
GlobalBest.Cost = float()
 
BestCost=np.zeros((MaxIt,1))
print("Generate initial solutions ...")
for i in range(1, nPop):
    A = np.random.randint(VarMin, VarMax, [1, nVar])
    
pass
