import qiskit
from qiskit import IBMQ

# Load account from disk:
provider = IBMQ.load_account()
# list the account currently in the session
print(IBMQ.active_account())
# list all available providers
print(IBMQ.providers())
print(provider.backends())

