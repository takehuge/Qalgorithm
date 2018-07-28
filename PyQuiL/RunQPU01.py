from pyquil.api import get_devices, QPUConnection
from pyquil.quil import Program
from pyquil.gates import *

import time

devices = get_devices()
devs = []
for device in devices:
    if device.is_online():
        print('Device {} is online'.format(device.name))
        devs.append(device.name)

i = int(input("Which device do you wanna use? (1 and above) "))
dev = devs[i - 1]

print("device name: ", dev)
qpu = QPUConnection(dev)

devices = get_devices(as_dict=True)
selected = devices['8Q-Agave']
qubits = selected.specs.qubits_specs

# print("SPECS:")
# for spec in qubits:
#         print(spec)

def gen():
    for spec in selected.specs.qubits_specs:
        yield spec

print("\nGenerating Specs: ")
g = gen()
for i in g:
    print(i)
    # print('\n#{}: '.format(i), next(g))
    time.sleep(1)

# p = Program(H(0), CNOT(0, 1), MEASURE(0, 0),
#             MEASURE(0, 1), MEASURE(1, 0), MEASURE(1, 1))
# job_id = qpu.run_async(p, [0,1], 1000)
# while not qpu.get_job(job_id).is_done:
#     print("still on the way...")
#     time.sleep(5)
# print(qpu.get_job(job_id).result())


