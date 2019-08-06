from qiskit import IBMQ

IBMQ.load_account()
print('Available Providers: ')
IBMQ.providers()

