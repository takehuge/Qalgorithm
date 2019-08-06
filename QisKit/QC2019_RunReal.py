import qiskit
from qiskit import IBMQ, QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

# Load IBMQ account:
provider = IBMQ.load_account()

# Registration:
q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.cx(q[0],q[1])
qc.measure(q[0],c[0])
qc.measure(q[1],c[1])

print("Quantum Circuit:\n %s" %qc)

# run for real
job = qiskit.execute(qc, provider.get_backend('ibmq_16_melbourne'))
result = job.result()

print(job.job_id())

