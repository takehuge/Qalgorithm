from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import CNOT, H

qvm = QVMConnection()
p = Program(H(0), CNOT(0, 1))

wf = qvm.wavefunction(p)
print(wf)
