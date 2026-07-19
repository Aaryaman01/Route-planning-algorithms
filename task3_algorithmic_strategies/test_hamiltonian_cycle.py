from task3_algorithmic_strategies.hamiltonian_cycle import (
    hamiltonian_cycle
)


graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]


cycle = hamiltonian_cycle(graph)

print("Hamiltonian cycle:", cycle)