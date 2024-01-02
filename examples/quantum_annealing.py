# # INPUTS:
# # tot deltaT
# # n discretisation step
#
# define S wrt to T (T=0 => 0 T=1 => 1) --- make evolution linear
# start with |+>**n
# check intermediate and final states
#
# check fidelity between states (scalar product between expected and actual
# [remember that you have to compute the complex conjugate]) of the final
# hamiltonian (because you know it) find eigenvector and eigenvalue
# normalize
#
# example with one solution
# example with degenerate solution (fidelity with respect to subspace)
#
# try to do the same with Qiskit

from qumess.operators import X, Y, Z, I