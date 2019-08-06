import matplotlib
matplotlib.use('tkAgg')

import numpy as np
from qiskit import ( QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer)
from qiskit.visualization import plot_histogram

q = QuantumRegister(5, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)

circ.h(q[0])
circ.cx(q[0],q[1])
circ.measure(q[0],c[0])
circ.measure(q[1],c[1])

# circ.draw(output='mpl')
print(circ)
simulator = Aer.get_backend('qasm_simulator')
job = execute(circ, simulator, shots=1000)
result = job.result()
counts = result.get_counts(circ)
print("\nTotal count for 0 and 11 are: %s" %counts)

plot_histogram(counts)

