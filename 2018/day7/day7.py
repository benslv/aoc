from collections import defaultdict

edges = defaultdict(list)
degree = defaultdict(int)

"""
Create a dictionary entry for each process, detailing which processes it depends on to finish first.
"""
for line in open("day7.test", "r").readlines():
    words = line.split(" ")
    x = words[1]
    y = words[7]
    edges[x].append(y)
    degree[y] += 1

"""
Sort the edges alphabetically, as this is how dependent processes are handled.
"""
for k in edges:
    edges[k] = sorted[edges[k]]
