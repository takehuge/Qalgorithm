from qiskit import version
version._get_qiskit_versions()

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import BasicAer, execute

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

qr = QuantumRegister(1, 'q')

def vqe_ansatz(theta):
    var_circ= QuantumCircuit(qr)
    var_circ.ry(theta,qr)
    return var_circ

### Select simulator
QC_simulator = BasicAer.get_backend('qasm_simulator')

# Define number of measurments shots
sample_shots=10000

cr = ClassicalRegister(1, 'c')
def expval(parameter):
    
    # Call ansatz
    circ_in=vqe_ansatz(parameter)
    
    # Measure in z basis
    Zmeas = QuantumCircuit(qr, cr)
    Zmeas.barrier(qr)
    Zmeas.measure(qr,cr)
    vqe=circ_in+Zmeas
    # Compile and execute
    job_qasm = execute(vqe, QC_simulator, shots=sample_shots)
    result_sim = job_qasm.result().get_counts()
    # Calculate expectation
    P_0=result_sim.get('0',0)/sample_shots
    P_1=result_sim.get('1',0)/sample_shots
    vqe_Z=P_0-P_1

    # Measure in x basis
    Zmeas = QuantumCircuit(qr, cr)
    Zmeas.barrier(qr)
    Zmeas.ry(-np.pi/2, qr)
    Zmeas.measure(qr,cr)
    vqe=circ_in+Zmeas
    # Compile and execute
    job_qasm = execute(vqe, QC_simulator, shots=sample_shots)
    result_sim = job_qasm.result().get_counts()
    # Calculate expectation
    P_0=result_sim.get('0',0)/sample_shots
    P_1=result_sim.get('1',0)/sample_shots
    vqe_X=P_0-P_1
    
    vqe_ans = 0.789689*vqe_Z + 0.181210*vqe_X -1.0421749
    return vqe_ans

test_expval=expval(0.5)
print("Expectation value : {}".format(test_expval))

theta_range = np.linspace(0.0, 2 * np.pi, 100)
vqe_result=[expval(params) for params in theta_range]

plt.xlabel('theta')
plt.ylabel('Expectation value')
plt.plot(theta_range, vqe_result)
plt.show()

print("The lowest eigenvalue: {0} \t corresponding parameters: {1}".format(min(vqe_result),theta_range[vqe_result.index(min(vqe_result))]))

# optimizer
initial_guess=[0]
ans=minimize(expval,initial_guess,method='COBYLA')
print(ans)
