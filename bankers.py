#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bankers_algorithm(available, maximum, allocation):
    num_processes = len(available)
    num_resources = len(available[0])

    need = []
    for i in range(num_processes):
        need.append([maximum[i][j] - allocation[i][j] for j in range(num_resources)])

    work = available[:]
    finish = [False] * num_processes

    safe_sequence = []
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        if not found:
            break

    if all(finish):
        return True, safe_sequence
    else:
        return False, []


available_resources = [3, 3, 2]

maximum_resources = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

allocated_resources = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

is_safe, safe_sequence = bankers_algorithm(available_resources, maximum_resources, allocated_resources)

if is_safe:
    print("The system is in a safe state.")

