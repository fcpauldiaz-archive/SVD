import numpy as np

mat = np.matrix([[2,1],[3,4]])
U_svd, sigma, V_svd  = np.linalg.svd(mat)
#print U_svd, "U"
#print sigma, "sigma"
#print V_svd, "V"
U =  np.matrix(U_svd)
D =  np.diag(sigma) #obtener solo la diagonal
V =  np.matrix(V_svd)
S = U*D*V
print abs((U*V) - mat) 
print U
print np.linalg.inv(V)

print np.linalg.norm(S) - np.linalg.norm(mat)